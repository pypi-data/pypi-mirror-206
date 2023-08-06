from __future__ import annotations

__all__ = ["Students"]

from typing import Dict
from typing import List
from typing import cast

from ._types import Content
from .base import BaseEndpoint


class Students(BaseEndpoint):
    """Students endpoint"""

    __path = "students"

    __slots__ = ()

    def list(self) -> List[Content]:
        """List of students."""

        result = self._client.get(f"{self.__path}/")
        content = cast(Dict[str, List[Content]], result.content)
        return content.get("students", [])

    def delete(self, student: str) -> bool:
        """Delete a student.

        :param student: Student id.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/{student}/")
        return result.status == 204
