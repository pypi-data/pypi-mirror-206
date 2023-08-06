from __future__ import annotations

__all__ = ["File"]

from typing import Dict
from typing import List
from typing import Optional
from typing import cast

from pawapi.exceptions import BadRequestError
from pawapi.exceptions import NotFoundError

from ._types import Content
from .base import BaseEndpoint


class File(BaseEndpoint):
    """File endpoint"""

    __path = "files"

    __slots__ = ()

    def get_file_content(self, path: str) -> Optional[bytes]:
        """Retruns file contents.

        :param path: Path to file.
        :returns: File content or None if path is not a file.
        """

        content = self._client.get(f"{self.__path}/path{path}").content
        return cast(bytes, content) if isinstance(content, bytes) else None

    def get_directory_content(self, path: str) -> Optional[Content]:
        """Returns directory content.

        :param path: Path to directory.
        :returns: Directory content or None if path is not a directory.
        """

        content = self._client.get(f"{self.__path}/path{path}").content
        return cast(Content, content) if isinstance(content, dict) else None

    def upload(self, path: str, file_content: bytes) -> bool:
        """Uploads a file.

        :param path: File destination.
        :param file_content: File content.
        :returns: True if file has been created, False if file has been updated.
        """

        result = self._client.post(
            path=f"{self.__path}/path{path}",
            files={"content": file_content},
        )
        return result.status == 201

    def delete(self, path: str) -> bool:
        """Remove file or directory.

        .. warning::

            Directory will be removed recursively.

        :param path: Path to file or directory.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/path{path}")
        return result.status == 204

    def start_sharing(self, path: str) -> str:
        """Share content.

        :param path: Path to file or directory.
        :returns: URL to shared content.
        """

        result = self._client.post(
            path=f"{self.__path}/sharing/",
            data={"path": path},
        )
        content = cast(Dict[str, str], result.content)
        return content["url"]

    def get_sharing_status(self, path: str) -> Optional[str]:
        """Sharing status for a path.

        :param path: Path to file or directory.
        :returns: URL to shared content or None.
        """

        try:
            result = self._client.get(
                f"{self.__path}/sharing/",
                {"path": path},
            )
        except NotFoundError:
            return None

        content = cast(Dict[str, str], result.content)
        return content["url"]

    def stop_sharing(self, path: str) -> bool:
        """Stop sharing.

        :param path: Path to file or directory.
        :returns: True on success.
        """

        result = self._client.delete(
            path=f"{self.__path}/sharing/",
            params={"path": path},
        )
        return result.status == 204

    def get_tree(self, path: str) -> Optional[List[str]]:
        """Returns a list of the contents of a directory, and its
        subdirectories (up to 1000 entries). Paths ending in slash ("/")
        represent directories.

        :param path: Path to directory.
        :returns: Directory content or None if path is a file or does not exist.
        """

        try:
            result = self._client.get(
                f"{self.__path}/tree/",
                {"path": path},
            )
        except BadRequestError:  # returns status 400 if path does not exist
            return None

        return cast(List[str], result.content)
