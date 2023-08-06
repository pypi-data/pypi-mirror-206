from __future__ import annotations

__all__ = ["Pawapi"]

from typing import Optional

from .api import AlwaysOnTask
from .api import Console
from .api import Cpu
from .api import File
from .api import Python
from .api import ScheduledTask
from .api import Students
from .api import System
from .api import Webapp
from .client import Client
from .region import Region
from .utils import validate_credentials


class Pawapi:
    """Main `pawapi` object.

    Usage::

        token = '<your_token>'
        user = '<your_username>'

        api = Pawapi(user, token)
        print(api.cpu.get_info())

    :param username: PythonAnywhere username.
    :param token: API token.
    :param region: Account region.
    :param timeout: Request timeout.
    """

    __slots__ = (
        "_username",
        "_region",
        "_client",
        "_alwayson_task",
        "_console",
        "_cpu",
        "_file",
        "_python",
        "_scheduled_task",
        "_students",
        "_system",
        "_webapp",
    )

    def __init__(
        self,
        username: str,
        token: str,
        *,
        region: Region = Region.US,
        timeout: float = 8,
    ) -> None:
        validate_credentials("username", username)
        validate_credentials("token", token)

        self._username = username
        self._region = region

        self._client = Client(
            username=username,
            token=token,
            region=region,
            timeout=timeout,
        )

        self._alwayson_task: Optional[AlwaysOnTask] = None
        self._console: Optional[Console] = None
        self._cpu: Optional[Cpu] = None
        self._file: Optional[File] = None
        self._python: Optional[Python] = None
        self._scheduled_task: Optional[ScheduledTask] = None
        self._students: Optional[Students] = None
        self._system: Optional[System] = None
        self._webapp: Optional[Webapp] = None

    def __str__(self) -> str:
        return f"{self._region.value}:{self._username}"

    def __repr__(self) -> str:
        return f"<Pawapi [{self._region.value}:{self._username}]>"

    @property
    def username(self) -> str:
        return self._username

    @property
    def region(self) -> Region:
        return self._region

    @property
    def console(self) -> Console:
        """Console endpoint.

        See: :class:`pawapi.api.Console`
        """

        if self._console is None:
            self._console = Console(self._client)
        return self._console

    @property
    def cpu(self) -> Cpu:
        """Cpu endpoint.

        See: :class:`pawapi.api.Cpu`
        """

        if self._cpu is None:
            self._cpu = Cpu(self._client)
        return self._cpu

    @property
    def file(self) -> File:
        """File endpoint.

        See: :class:`pawapi.api.File`
        """

        if self._file is None:
            self._file = File(self._client)
        return self._file

    @property
    def python(self) -> Python:
        """Python endpoint.

        See: :class:`pawapi.api.Python`
        """

        if self._python is None:
            self._python = Python(self._client)
        return self._python

    @property
    def scheduled_task(self) -> ScheduledTask:
        """Scheduled task ednpoint.

        See: :class:`pawapi.api.ScheduledTask`
        """

        if self._scheduled_task is None:
            self._scheduled_task = ScheduledTask(self._client)
        return self._scheduled_task

    @property
    def students(self) -> Students:
        """Students endpoint.

        See: :class:`pawapi.api.Students`
        """

        if self._students is None:
            self._students = Students(self._client)
        return self._students

    @property
    def system(self) -> System:
        """System endpoint.

        See: :class:`pawapi.api.System`
        """

        if self._system is None:
            self._system = System(self._client)
        return self._system

    @property
    def alwayson_task(self) -> AlwaysOnTask:
        """Always-On task endpoint

        See: :class:`pawapi.api.AlwaysOnTask`
        """

        if self._alwayson_task is None:
            self._alwayson_task = AlwaysOnTask(self._client)
        return self._alwayson_task

    @property
    def webapp(self) -> Webapp:
        """Webapp endpoint.

        See: :class:`pawapi.api.Webapp`
        """

        if self._webapp is None:
            self._webapp = Webapp(self._client)
        return self._webapp
