from __future__ import annotations

__all__ = ["BaseEndpoint"]

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from pawapi.client import Client


class BaseEndpoint:
    """Base class for endpoints.

    :param client: HTTP client.
    """

    __slots__ = "_client"

    def __init__(self, client: Client) -> None:
        self._client = client

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__class__.__name__}>"
