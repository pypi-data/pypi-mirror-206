from __future__ import annotations

__all__ = ["Cpu"]

from typing import cast

from ._types import Content
from .base import BaseEndpoint


class Cpu(BaseEndpoint):
    """Cpu endpoint"""

    __path = "cpu"

    __slots__ = ()

    def get_info(self) -> Content:
        """Returns information about cpu usage."""

        result = self._client.get(f"{self.__path}/")
        return cast(Content, result.content)
