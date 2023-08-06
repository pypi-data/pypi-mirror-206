from __future__ import annotations

__all__ = ["Python"]

from typing import TYPE_CHECKING
from typing import Union
from typing import cast

from ._types import Content
from .base import BaseEndpoint

if TYPE_CHECKING:  # pragma: no cover
    from pawapi.python import Python2
    from pawapi.python import Python3


class Python(BaseEndpoint):
    """Python endpoint"""

    __slots__ = ()

    def get_python_version(self) -> Content:
        """Returns current Python version and list of available versions."""

        content = self._client.get("default_python_version/").content
        return cast(Content, content)

    def set_python_version(
        self,
        version: Union[Python2, Python3],
    ) -> Content:
        """Set default Python version.

        :param version: Python version.
        """

        result = self._client.patch(
            path="default_python_version/",
            data={"default_python_version": version.format_value(short=True)},
        )
        return cast(Content, result.content)

    def get_python3_version(self) -> Content:
        """Returns current Python3 version and list of available versions."""

        result = self._client.get("default_python3_version/")
        return cast(Content, result.content)

    def set_python3_version(self, version: Python3) -> Content:
        """Set default Python3 version.

        :param version: Python version.
        """

        result = self._client.patch(
            path="default_python3_version/",
            data={"default_python3_version": version.format_value(short=True)},
        )
        return cast(Content, result.content)

    def get_sar_version(self) -> Content:
        """Retruns current Python version used for the 'Run' button
        in the editor and list of available versions.
        """

        result = self._client.get("default_save_and_run_python_version/")
        return cast(Content, result.content)

    def set_sar_version(self, version: Python3) -> Content:
        """Set Python version used for the 'Run' button in the editor.

        :param version: Python version.
        """

        # yapf: disable
        result = self._client.patch(
            path="default_save_and_run_python_version/",
            data={"default_save_and_run_python_version": version.format_value(short=True)},  # noqa: E501
        )
        # yapf: enable
        return cast(Content, result.content)
