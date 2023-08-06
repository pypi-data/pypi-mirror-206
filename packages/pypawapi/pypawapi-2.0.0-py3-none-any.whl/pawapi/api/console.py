from __future__ import annotations

__all__ = ["Console"]

from typing import TYPE_CHECKING
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from typing import cast

from ._types import Content
from .base import BaseEndpoint

if TYPE_CHECKING:  # pragma: no cover
    from pawapi.shell import Shell


class Console(BaseEndpoint):
    """Console endpoint"""

    __path = "consoles"

    __slots__ = ()

    def list(self) -> List[Content]:
        """Returns list of all your consoles."""

        content = self._client.get(f"{self.__path}/").content
        return cast(List[Content], content)

    def list_shared(self) -> List[Content]:
        """Returns list of all consoles shared with you."""

        result = self._client.get(f"{self.__path}/shared_with_you/")
        return cast(List[Content], result.content)

    def create(
        self,
        executable: Shell,
        *,
        arguments: Optional[str] = None,
        working_directory: Optional[str] = None,
    ) -> Optional[Content]:
        """Create a new console.

        .. note::

            Does not actually start the process. Open new console in the
            browser to initialize it.

        :param executable: Console executable (bash, pypy, etc.).
        :param arguments: Sturtup arguments for executable.
        :param working_directory: Startup directory for `executable`.
        :returns: Console info on success.
        """

        result = self._client.post(
            path=f"{self.__path}/",
            data={
                "executable": executable.value,
                "arguments": arguments,
                "working_directory": working_directory,
            },
        )
        return cast(Content, result.content) if result.status == 201 else None

    def get_info(self, console_id: Union[int, str]) -> Content:
        """Returns information about a console.

        :param console_id: Console id.
        """

        result = self._client.get(f"{self.__path}/{console_id}/")
        return cast(Content, result.content)

    def kill(self, console_id: Union[int, str]) -> bool:
        """Kill a console.

        :param console_id: Console id.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/{console_id}/")
        return result.status == 204

    def get_output(self, console_id: Union[int, str]) -> str:
        """Returns recent command output (up to 500 characters).

        :param console_id: Console id.
        """

        result = self._client.get(
            f"{self.__path}/{console_id}/get_latest_output/"
        )
        content = cast(Dict[str, str], result.content)
        return content.get("output", "")

    def send_input(
        self,
        console_id: Union[int, str],
        command: str,
    ) -> bool:
        """Send input into the console.

        .. note::

            Add a '\\n' at the end of ``command`` to actually execute it.

        :param console_id: Console id.
        :param command: Command to execute.
        :returns: True on success.
        """

        result = self._client.post(
            path=f"{self.__path}/{console_id}/send_input/",
            data={"input": command},
        )
        content = cast(Dict[str, str], result.content)
        return content["status"] == "OK"
