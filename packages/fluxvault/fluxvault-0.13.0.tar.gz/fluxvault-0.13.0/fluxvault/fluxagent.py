from __future__ import annotations

import asyncio
import binascii
import importlib
import os
import pty
import ssl
import subprocess
import sys
import tempfile
from pathlib import Path
from enum import Enum

import aiofiles
import aioshutil
from aiofiles import os as aiofiles_os
from aiohttp import ClientSession
from bitcoin.signmessage import BitcoinMessage, VerifyMessage
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
)
from cryptography.x509.oid import ExtensionOID, NameOID
from fluxrpc.auth import SignatureAuthProvider
from fluxrpc.protocols.jsonrpc import JSONRPCProtocol
from fluxrpc.server import RPCServer
from fluxrpc.transports.socket.server import EncryptedSocketServerTransport
from rich.pretty import pprint

from fluxvault.constants import STATE_SIG, WWW_ROOT, PLUGIN_DIR, SSL_DIR
from fluxvault.extensions import FluxVaultExtensions
from fluxvault.helpers import (
    AppMode,
    ContainerState,
    bytes_to_human,
    get_app_and_component_name,
)
from fluxvault.log import log
from fluxvault.registrar import FluxAgentRegistrar, FluxPrimaryAgent, FluxSubAgent


class FluxAgentException(Exception):
    pass


class FluxAgent:
    """Runs on Flux nodes - waits for connection from FluxKeeper"""

    def __init__(
        self,
        bind_address: str = "0.0.0.0",
        bind_port: int = 8888,
        disable_webserver: bool = False,
        registrar: FluxAgentRegistrar | None = None,
        extensions: FluxVaultExtensions = FluxVaultExtensions(),
        # working_dir: str = tempfile.gettempdir(),
        whitelisted_addresses: list = ["127.0.0.1"],
        verify_source_address: bool = False,
        signed_vault_connections: bool = False,
        auth_id: str = "",
        subordinate: bool = False,
        primary_agent: FluxPrimaryAgent | None = None,
    ):
        self.disable_webserver = disable_webserver
        self.extensions = extensions
        self.loop = asyncio.get_event_loop()
        self.auth_id = auth_id
        # self.working_dir = working_dir
        self.subordinate = subordinate
        self.registrar = registrar
        self.signed_vault_connections = signed_vault_connections
        self.bind_address = bind_address
        self.bind_port = bind_port
        self.whitelisted_addresses = whitelisted_addresses
        self.verify_source_address = verify_source_address
        self.primary_agent = primary_agent
        self.component_name, self.app_name = get_app_and_component_name()
        self.file_handles: dict = {}
        self.app_mode = AppMode.UNKNOWN
        self.container_state = ContainerState.DEFAULT

        log.info(f"Component name: {self.component_name}, App name: {self.app_name}")

        if not self.signed_vault_connections and not self.verify_source_address:
            # Must verify source address as a minimum
            self.verify_source_address = True

        # remove all this run_until_complete garbage
        self.setup_registrar()
        self.auth_provider = self.loop.run_until_complete(self.get_auth_provider())

        # Review all this stuff
        if self.app_mode in [AppMode.FILESERVER, AppMode.UNKNOWN]:
            self.loop.run_until_complete(self.validate_prior_state())

        self.raise_on_state_errors()
        self.register_extensions()

        self.loop.run_until_complete(self.setup_sub_agent())

        transport = EncryptedSocketServerTransport(
            bind_address,
            bind_port,
            whitelisted_addresses=whitelisted_addresses,
            verify_source_address=self.verify_source_address,
            auth_provider=self.auth_provider,
        )
        self.rpc_server = RPCServer(transport, JSONRPCProtocol(), self.extensions)

    @staticmethod
    async def get_app_owner_zelid(app_name: str) -> str:
        # ToDo: move this to helpers
        async with ClientSession() as session:
            async with session.get(
                f"https://api.runonflux.io/apps/appowner?appname={app_name}"
            ) as resp:
                data = await resp.json()
                zelid = data.get("data", "")
        return zelid

    async def setup_sub_agent(self):
        if self.subordinate:
            self.sub_agent = FluxSubAgent(
                self.component_name,
                self.app_name,
                self.primary_agent,
                address=self.bind_address,
            )
            await self.sub_agent.register_with_primary_agent()

    async def set_mode(self, mode: int):
        """Sets App mode and updates state to RUNNING"""
        self.app_mode = AppMode(mode)
        self.container_state = ContainerState.RUNNING

        match self.app_mode:
            case AppMode.FILESERVER:
                WWW_ROOT.mkdir(parents=True, exist_ok=True)
                self.registrar.enable_services()

    async def load_manifest(self, remote_fileserver_hash, sig):
        local_fileserver_hash = await self.crc_directory(WWW_ROOT, 0)
        if local_fileserver_hash != remote_fileserver_hash:
            log.error(
                f"local hash: {local_fileserver_hash} does not match remote: {remote_fileserver_hash}"
            )
            return

        with open(STATE_SIG, "wb") as stream:
            stream.write(sig)

    async def validate_prior_state(self):
        raw_state = None

        # fix this all up, should only run for fileserer

        if not self.auth_provider:
            # we can only validate prior state if we have an auth provider
            log.warn(
                "No auth provider set so unable to validate prior state... waiting for Keeper to connect"
            )
            return

        if not WWW_ROOT.exists():
            log.debug(
                f"Fileserver root {WWW_ROOT} does not exist... waiting for Keeper to connect"
            )
            return

        # if this file exists, means we're fileserver???
        if STATE_SIG.exists():
            with open(STATE_SIG, "rb") as stream:
                sig = stream.read()
        else:
            return

        current_vault_dir_hash = await self.crc_directory(WWW_ROOT, 0)
        msg = BitcoinMessage(str(current_vault_dir_hash))

        if VerifyMessage(self.auth_provider.address, msg, sig):
            log.info("Manifest validated... enabling fileserver endpoint")
            # shouldn't need try except here as we've validated
            # state = yaml.safe_load(raw_state)
            self.app_mode = AppMode.FILESERVER
            self.registrar.enable_services()
        else:
            log.error(
                "Manifest is different than signature... waiting for keeper to connect"
            )

    def setup_registrar(self):
        # At this point, the keeper hasn't made contact. However,
        # we may have just rebooted or something. If we still have the signature,
        # and a valid manifest - we can start serving without the keeper having made
        # contact
        enable_fileserver = False
        if self.registrar:
            self.registrar.app_name = self.app_name

        if not self.registrar:
            if self.app_mode == AppMode.FILESERVER:
                enable_fileserver = True
            self.registrar = FluxAgentRegistrar(
                self.app_name, enable_fileserver=enable_fileserver
            )
        # # this only happens if we've validated manifest
        # if self.app_mode == AppMode.FILESERVER:
        #     self.registrar.ready_to_serve

    def raise_on_state_errors(self):
        """Minimal tests to ensure we are good to run"""
        # try:
        #     os.listdir(self.working_dir)
        # except Exception as e:
        #     raise FluxAgentException(f"Error accessing working directory: {e}")

        if self.verify_source_address and not self.whitelisted_addresses:
            raise ValueError(
                "Whitelisted addresses must be provided if not signing connections"
            )

        if self.subordinate and not self.primary_agent:
            raise ValueError("Primary agent must be provided if subordinate")

    def register_extensions(self):
        self.extensions.add_method(self.get_all_object_hashes)
        self.extensions.add_method(self.write_object)
        self.extensions.add_method(self.remove_objects)
        self.extensions.add_method(self.get_methods)
        self.extensions.add_method(self.get_subagents)
        self.extensions.add_method(self.generate_csr)
        self.extensions.add_method(self.install_cert)
        self.extensions.add_method(self.install_ca_cert)
        self.extensions.add_method(self.upgrade_to_ssl)
        self.extensions.add_method(self.load_plugins)
        self.extensions.add_method(self.list_server_details)
        self.extensions.add_method(self.connect_shell)
        self.extensions.add_method(self.disconnect_shell)
        self.extensions.add_method(self.get_state)
        self.extensions.add_method(self.get_container_state)
        self.extensions.add_method(self.get_directory_hashes)
        self.extensions.add_method(self.set_mode)
        self.extensions.add_method(self.load_manifest)
        self.extensions.add_method(self.ping)
        # self.extensions.add_method(self.enable_registrar_fileserver)
        # self.extensions.add_method(self.run_entrypoint)

    async def get_auth_provider(self):
        auth_provider = None
        if self.signed_vault_connections:
            # this is solely for testing without an app (outside of a Fluxnode)
            if self.auth_id:
                address = self.auth_id
            else:
                address = await self.get_app_owner_zelid(self.app_name)
            log.info(f"App AuthID is: {address}")
            auth_provider = SignatureAuthProvider(address=address)
        return auth_provider

    def run(self):
        if not self.disable_webserver:
            self.loop.create_task(self.registrar.start_app())

        task = self.loop.create_task(self.rpc_server.serve_forever())

        try:
            self.loop.run_forever()
        finally:
            task.cancel()
            if not self.disable_webserver:
                self.loop.run_until_complete(self.registrar.cleanup())

    async def run_async(self):
        if not self.disable_webserver:
            self.loop.create_task(self.registrar.start_app())
            log.info(
                f"Sub agent http server running on port {self.registrar.bind_port}"
            )

        self.loop.create_task(self.rpc_server.serve_forever())

    async def upgrade_to_ssl(self):
        cert = tempfile.NamedTemporaryFile()
        key = tempfile.NamedTemporaryFile()
        ca_cert = tempfile.NamedTemporaryFile()
        with open(cert.name, "wb") as f:
            f.write(self.cert)
        with open(key.name, "wb") as f:
            f.write(self.key)
        with open(ca_cert.name, "wb") as f:
            f.write(self.ca_cert)

        log.info("Upgrading connection to SSL")
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(cert.name, keyfile=key.name)
        context.load_verify_locations(cafile=ca_cert.name)
        context.check_hostname = False
        context.verify_mode = ssl.VerifyMode.CERT_REQUIRED
        # context.set_ciphers("ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384")

        cert.close()
        key.close()
        ca_cert.close()

        transport = EncryptedSocketServerTransport(
            self.bind_address,
            self.bind_port + 1,
            whitelisted_addresses=self.whitelisted_addresses,
            verify_source_address=self.verify_source_address,
            auth_provider=self.auth_provider,
            ssl=context,
        )
        await self.rpc_server.transport.stop_server()
        log.info("Non SSL RPC server stopped")
        self.rpc_server = RPCServer(transport, JSONRPCProtocol(), self.extensions)
        self.loop.create_task(self.rpc_server.serve_forever())

    def cleanup(self):
        # ToDo: look at cleanup for rpc server too
        if self.registrar:
            self.loop.run_until_complete(self.registrar.cleanup())

    def opener(self, path, flags):

        return os.open(path, flags, 0o777)

    ### EXTERNAL METHODS CALLED FROM KEEPER BELOW HERE ###

    def get_methods(self) -> dict:
        """Returns methods available for the keeper to call"""
        return {k: v.__doc__ for k, v in self.extensions.method_map.items()}

    def get_container_state(self) -> str:
        # todo, sort out this serialization stuff
        return self.container_state.value

    def get_state(self) -> dict:
        methods = self.get_methods()
        plugins = self.extensions.list_plugins()
        primary_agent = self.primary_agent.to_dict() if self.primary_agent else None
        return {
            "methods": methods,
            "plugins": plugins,
            "component_name": self.component_name,
            "app_name": self.app_name,
            "enable_registrar": self.disable_webserver,
            "auth_id": self.auth_id,
            # "working_dir": self.working_dir,
            "subordinate": self.subordinate,
            "signed_vault_connections": self.signed_vault_connections,
            "bind_address": self.bind_address,
            "bind_port": self.bind_port,
            "whitelisted_addresses": self.whitelisted_addresses,
            "verify_source_address": self.verify_source_address,
            "primary_agent": primary_agent,
        }

    async def crc_file(self, filename: Path, crc: int) -> int:
        crc = binascii.crc32(filename.name.encode(), crc)

        # should this be chunked like on the Keeper? Or remove chunk?
        try:
            async with aiofiles.open(filename, "rb") as f:
                data = await f.read()
                crc = binascii.crc32(data, crc)
        except PermissionError:
            log.error(
                f"Permission error reading file {filename}. Unable to checksum. Skipping"
            )
            # do something here?!?
        except Exception as e:
            log.error(f"Unknown error reading file: {repr(e)}")

        return crc

    async def crc_directory(self, directory: Path, crc: int) -> int:
        crc = binascii.crc32(directory.name.encode(), crc)
        for path in sorted(directory.iterdir(), key=lambda p: str(p).lower()):
            crc = binascii.crc32(path.name.encode(), crc)

            if path.is_file():
                crc = await self.crc_file(path, crc)
            elif path.is_dir():
                crc = await self.crc_directory(path, crc)
        return crc

    async def get_object_crc(self, path: str) -> int:
        p = Path(path)

        if not p.exists():
            crc = 0

        elif p.is_dir():
            crc = await self.crc_directory(p, 0)

        elif p.is_file():
            crc = await self.crc_file(p, 0)

        return {"name": path, "crc32": crc}

    async def get_all_object_hashes(self, objects: list) -> list:
        """Returns the crc32 for each object that is being managed"""
        log.info(f"Returning crc's for {len(objects)} object(s)")
        tasks = []
        for obj in objects:
            tasks.append(self.loop.create_task(self.get_object_crc(obj)))
        results = await asyncio.gather(*tasks)

        return results

    async def get_file_hash(self, file: Path):
        crc = await self.crc_file(file, 0)
        return {str(file): crc}

    async def get_directory_hashes(self, dir: str):
        """Hashes up all files in a specific directory. if
        give relative path, out working dir is base path. Need
        to remove this again for each hash to give back common path format"""
        hashes = {}
        p = Path(dir)
        try:
            if not p.exists():
                return hashes

            crc = binascii.crc32(p.name.encode())

            hashes.update({str(p): crc})
            for path in sorted(p.iterdir(), key=lambda p: str(p).lower()):
                if path.is_dir():
                    hashes.update(await self.get_directory_hashes(str(path)))

                elif path.is_file():
                    hashes.update(await self.get_file_hash(path))
        except Exception as e:
            print(repr(e))
            raise

        return hashes

    async def remove_object(self, obj: str):
        p = Path(obj)

        if p.exists():
            if p.is_dir():
                await aioshutil.rmtree(p)
            elif p.is_file():
                await aiofiles_os.remove(p)

    async def write_objects(self, objects: list):
        for obj in objects:
            log.info(f"Writing object {obj['path']}")
            await self.write_object(**obj)

    async def write_object(self, path, is_dir, data) -> bool:
        # ToDo: brittle file path
        # ToDo: catch file PermissionError etc
        log.info(
            f"In write object RPC method, writing: {bytes_to_human(len(data))} Path: {path}"
        )
        executable = False  # pass this in dict in future

        p = Path(path)

        p.parent.mkdir(parents=True, exist_ok=True)

        if is_dir:
            p.mkdir(parents=True, exist_ok=True)
            return

        if isinstance(data, bytes):
            mode = "wb"
        elif isinstance(data, str):
            mode = "w"
        else:
            raise ValueError("Data written must be either str or bytes")

        opener = self.opener if executable else None
        try:
            async with aiofiles.open(p, mode=mode, opener=opener) as file:
                await file.write(data)
        # ToDo: tighten this up
        except Exception as e:
            print("exception opening / writing file")
            log.error(repr(e))

        # else:  # tarball
        #     fh = io.BytesIO(obj["data"])
        #     try:
        #         with tarfile.open(fileobj=fh, mode="r|bz2") as tar:
        #             tar.extractall(str(p))
        #         return
        #     except Exception as e:
        #         print(f"Tarfile error: {repr(e)}")

    async def get_subagents(self):
        agents = {}
        if self.registrar:
            agents = {v.dns_name: v.as_dict() for v in self.registrar.sub_agents}
        return {"sub_agents": agents}

    async def remove_objects(self, objects: list):
        for obj in objects:
            log.info(f"Removing object {obj}")
            await self.remove_object(obj)

    async def connect_shell(self, peer):
        # peer is the source ip, host
        # json converts tuple to list
        peer = tuple(peer)

        child_pid, fd = pty.fork()
        if child_pid == 0:

            # Child process
            while log.hasHandlers():
                log.removeHandler(log.handlers[0])

            try:
                subprocess.run("zsh")
            except:
                pass

        else:
            # Parent process

            # the peer may be the jumphost instead of actual browser,
            # we have no way of identifying if they are a jumphost so we
            # pass the RPCClient id of the originating request
            try:
                self.rpc_server.transport.attach_pty(child_pid, fd, peer)
                await self.rpc_server.transport.proxy_pty(peer)
            except Exception as e:
                print("In connect_shell")
                print(repr(e))

    async def disconnect_shell(self, peer):
        log.info(f"Disconnecting shell for peer: {peer[0]}")
        peer = tuple(peer)  # json convert to list
        self.rpc_server.transport.detach_pty(peer)

    def list_server_details(self):
        return {
            # "working_dir": self.working_dir,
            "plugins": self.extensions.list_plugins(),
            "registrar_disabled": self.disable_webserver,
        }

    def enable_registrar_fileserver(self):
        if self.registrar:
            self.registrar.ready_to_serve = True

    async def load_plugins(self, directory: str = PLUGIN_DIR):
        p = Path(directory)

        log.info(f"loading plugins from directory {p}")

        # print(os.getcwd())
        sys.path.append(str(p))

        # or p.stat().st_size == 0:
        p.mkdir(parents=True, exist_ok=True)

        plugins = [
            f.name.rstrip(".py")
            for f in p.iterdir()
            if not f.is_dir() and not str(f).endswith("runner.py")
        ]

        log.info(f"Plugins available: {plugins}")

        for f in plugins:
            importlib.invalidate_caches()
            # ToDo: wrap try / except
            try:
                plugin = importlib.import_module(f)
            except Exception as e:
                log.error(e)
            plugin = plugin.plugin
            # tidy up
            if isinstance(plugin, FluxVaultExtensions):
                if plugin.required_packages:
                    log.info(
                        f"Installing the following packages: {plugin.required_packages}"
                    )
                    try:
                        subprocess.run(
                            [sys.executable, "-m", "pip", "install"]
                            + plugin.required_packages,
                            check=True,
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT,
                        )
                    except subprocess.CalledProcessError:
                        log.error("Error loading extensions packages, skipping")
                        return
                    try:
                        runner = importlib.import_module(f"{f}_runner")
                    except Exception as e:
                        print(repr(e))
                    else:
                        plugin = runner.plugin
                        if not isinstance(plugin, FluxVaultExtensions):
                            log.error(
                                f"Bad runner... plugin is not a FluxVault extensions"
                            )

                self.extensions.add_plugin(plugin)
                log.info(f"Plugin {plugin.plugin_name} loaded")
            else:
                log.error("Plugin load error... skipping")

    async def generate_csr(self, fqdn: str = "", keyname: str = "id_rsa"):
        # ToDo: this needs to include a Fluxnode identifier
        altname = fqdn if fqdn else f"{self.component_name}.{self.app_name}.com"

        log.info(f"Generating CSR with altname {altname}")

        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        # we want to save the key to file
        if fqdn:
            path = SSL_DIR / keyname
            with open(path, "w") as stream:
                stream.write(
                    key.private_bytes(
                        Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
                    ).decode()
                )
        else:
            self.key = key.private_bytes(
                Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
            )

        # public = key.public_key().public_bytes(
        #     Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
        # )

        csr = (
            x509.CertificateSigningRequestBuilder()
            .subject_name(
                x509.Name(
                    [
                        x509.NameAttribute(NameOID.COMMON_NAME, altname),
                    ]
                )
            )
            .add_extension(
                x509.SubjectAlternativeName(
                    [
                        x509.DNSName(altname),
                    ]
                ),
                critical=False,
            )
            .sign(key, hashes.SHA256())
        )
        return {"csr": csr.public_bytes(Encoding.PEM)}

    async def install_cert(self, cert_bytes: bytes, name: str = ""):
        if not name:
            self.cert = cert_bytes
            cert = x509.load_pem_x509_certificate(cert_bytes)
            issuer = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
            san = cert.extensions.get_extension_for_oid(
                ExtensionOID.SUBJECT_ALTERNATIVE_NAME
            ).value.get_values_for_type(x509.DNSName)
            log.info(f"Installing cert from issuer {issuer} with Alt names {san}")

            # ToDo: this timing seems a bit off?
            await self.sub_agent.update_local_agent(enrolled=True)
        else:
            path = SSL_DIR / name
            with open(path, "w") as stream:
                stream.write(cert_bytes.decode())

    async def upgrade_connection(self):
        self.rpc_server.transport.upgrade_socket()

    async def ping(self) -> str:
        return "PONG"

    async def install_ca_cert(self, cert_bytes: bytes):
        log.info("Installing CA cert")
        self.ca_cert = cert_bytes

    async def run_entrypoint(self, entrypoint: str):
        # ToDo: don't use shell
        proc = await asyncio.create_subprocess_shell(entrypoint)

        await proc.communicate()
