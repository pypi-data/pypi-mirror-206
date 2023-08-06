from __future__ import annotations

__all__ = ["System"]

from typing import TYPE_CHECKING
from typing import cast

from ._types import Content
from .base import BaseEndpoint

if TYPE_CHECKING:  # pragma: no cover
    from pawapi.system import SystemImage


class System(BaseEndpoint):
    """System endpoint"""

    __path = "system_image"

    __slots__ = ()

    def get_current_image(self) -> Content:
        """Returns current system image and list of available images."""

        result = self._client.get(f"{self.__path}/")
        return cast(Content, result.content)

    def set_image(self, system_image: SystemImage) -> Content:
        """Set system image.

        .. note::

            Use :meth:`System.get_current_image()` to get list of available
            system images.

        :param system_image: System image name.
        """

        result = self._client.patch(
            path=f"{self.__path}/",
            data={"system_image": system_image.value},
        )
        return cast(Content, result.content)
