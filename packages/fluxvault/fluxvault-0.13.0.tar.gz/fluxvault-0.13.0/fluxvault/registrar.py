from __future__ import annotations

import asyncio
import ipaddress
import os
from dataclasses import dataclass
from pathlib import Path

import aiofiles
from aiohttp import ClientConnectorError, ClientSession, ClientTimeout, web

from fluxvault.helpers import get_app_and_component_name
from fluxvault.log import log


@dataclass
class FluxPrimaryAgent:
    """Container to hold parent agent info"""

    name: str = "fluxagent"
    port: int = 2080
    address: str | None = None

    def to_dict(self):
        return self.__dict__


@dataclass
class FluxSubAgent:
    """Container for sub agent info"""

    name: str  # component name
    app_name: str
    parent: FluxPrimaryAgent | None = None
    dns_name: str = ""
    enrolled: bool = False
    address: str | None = None
    role: str = "NotAssigned"

    def as_dict(self):
        # maybe just self.__dict__ minus parent
        return {
            "name": self.name,
            "dns_name": self.dns_name,
            "app_name": self.app_name,
            "enrolled": self.enrolled,
            "address": self.address,
            "role": self.role,
        }

    def merge_existing(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    async def register_with_primary_agent(self):
        self.url = (
            f"http://flux{self.parent.name}_{self.app_name}:{self.parent.port}/register"
        )
        self.dns_name = f"flux{self.name}_{self.app_name}"

        if self.parent.address and self.parent.port:
            # this means were a subordinate and not on a flux node, basically testing
            self.url = f"http://{self.parent.address}:{self.parent.port}/register"
            self.dns_name = self.address

        registered = False
        while not registered:
            try:
                async with ClientSession(timeout=ClientTimeout(3)) as session:
                    async with session.post(self.url, json=self.as_dict()) as resp:
                        if resp.status == 202:
                            registered = True
            except (asyncio.exceptions.TimeoutError, ClientConnectorError):
                log.error(
                    f"Unable to connect to local fluxagent @ {self.url}... trying again in 5"
                )
                await asyncio.sleep(5)
        log.info("Successfully registered with primary agent")

    async def update_local_agent(self, **kwargs):
        self.merge_existing(**kwargs)

        self.url = (
            f"http://flux{self.parent.name}_{self.app_name}:{self.parent.port}/update"
        )

        if self.parent.address and self.parent.port:
            # this means were a subordinate and not on a flux node, basically testing
            self.url = f"http://{self.parent.address}:{self.parent.port}/update"

        try:
            async with ClientSession(timeout=ClientTimeout(3)) as session:
                async with session.post(self.url, json=self.as_dict()) as resp:
                    pass
        except (asyncio.exceptions.TimeoutError, ClientConnectorError):
            log.error("Unable to connect to local fluxagent...")
        log.info("Successfully updated with primary agent")


class FluxAgentRegistrar:
    def __init__(
        self,
        app_name: str | None = None,
        working_dir: str = "/tmp",
        bind_address: str = "0.0.0.0",
        bind_port: int = 2080,
        enable_fileserver: bool = False,
        # enable_registrar: bool = False,
    ):
        self.bind_address = bind_address
        self.bind_port = bind_port
        self.enable_fileserver = enable_fileserver
        # self.enable_registrar = enable_registrar
        self.app_name = app_name
        self.working_dir = working_dir
        self.sub_agents: list = []
        self.runners: list = []
        self.app = web.Application()
        self._ready_to_serve = False

    @property
    def ready_to_serve(self):
        # this gets set via the keeper
        return self._ready_to_serve

    @ready_to_serve.setter
    def read_to_serve(self, value: bool):
        self._ready_to_serve = value

    async def file_sender(file_path=None):
        """
        This function will read large file chunk by chunk and send it through HTTP
        without reading them into memory
        """
        async with aiofiles.open(file_path, "rb") as f:
            chunk = await f.read(64 * 1024)
            while chunk:
                yield chunk
                chunk = await f.read(64 * 1024)

    def enable_services(self):
        self.read_to_serve = True
        # if registrar:
        #     self.enable_registrar = registrar
        #     log.info(f"Sub agent http server running on port {self.bind_port}")

        # if fileserver:
        #     self.enable_fileserver = fileserver
        #     log.info(f"Enabling LAN fileserver on port {self.bind_port}")

    async def start_app(self):
        runner = web.AppRunner(self.app)
        # if self.enable_fileserver:
        #     self.enable_services()

        self.app.router.add_post("/register", self.handle_register)
        self.app.router.add_post("/update", self.handle_update)
        self.app.router.add_get("/file/{file_name:.*}", self.download_file)

        self.runners.append(runner)
        await runner.setup()
        site = web.TCPSite(runner, self.bind_address, self.bind_port)
        log.info(f"Starting http server on port {self.bind_port}")
        await site.start()

    async def download_file(self, request: web.Request) -> web.Response:
        # ToDo: Base downloads on component name
        # ToDo: Only auth once, not per request

        # We only accept connections from local network. (Protect against punter
        # exposing the fileserver port on the internet)

        # Flux bug: Flux is allocating outside rfc1918 so this is broken.

        # if not ipaddress.ip_address(request.remote).is_private:
        #     log.warn(
        #         f"Received request from non private ip address {request.remote}... unauthorized"
        #     )
        #     return web.Response(
        #         body="Unauthorized",
        #         status=403,
        #     )

        _, remote_app = get_app_and_component_name(request.remote)
        if remote_app != self.app_name:
            log.warn(
                f"Request from {request.remote} denied. {remote_app} does not match local: {self.app_name}"
            )
            return web.Response(
                body="Unauthorized",
                status=403,
            )
        if not self.ready_to_serve:
            return web.Response(
                body="Service unavailable - waiting for Keeper to connect",
                status=503,
            )

        file_path = Path(request.match_info["file_name"])
        # RESOLVE, check that length is longer than working dir
        if file_path.is_absolute():
            return web.Response(body="Invalid Path", status=403)

        headers = {"Content-disposition": f"attachment; filename={file_path.name}"}

        file_path = self.working_dir / file_path

        if not file_path.exists():
            return web.Response(
                body=f"File <{file_path.name}> does not exist",
                status=404,
            )

        return web.Response(
            body=FluxAgentRegistrar.file_sender(file_path=file_path), headers=headers
        )

    async def handle_update(self, request: web.Request) -> web.Response:
        # ToDo: Errors
        data = await request.json()
        sub_agent = FluxSubAgent(**data)

        self.sub_agents.append(sub_agent)
        self.log.info(
            f"Sub agent updated {sub_agent.dns_name}, enrolled: {sub_agent.enrolled}"
        )
        return web.Response(
            status=202,
        )

    async def handle_register(self, request: web.Request) -> web.Response:
        data = await request.json()
        sub_agent = FluxSubAgent(**data)

        self.sub_agents.append(sub_agent)
        self.log.info(
            f"New sub agent registered {sub_agent.dns_name} with role {sub_agent.role}"
        )
        return web.Response(
            status=202,
        )

    async def cleanup(self):
        for runner in self.runners:
            await runner.cleanup()
