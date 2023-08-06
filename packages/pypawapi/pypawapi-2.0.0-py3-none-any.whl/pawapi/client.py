from __future__ import annotations

__all__ = ["Client"]

from dataclasses import dataclass
from typing import Dict
from typing import Optional
from typing import Union

import requests

from .exceptions import BadRequestError
from .exceptions import InvalidJSONError
from .exceptions import InvalidTokenError
from .exceptions import NotFoundError
from .exceptions import PermissionDeniedError
from .exceptions import RequestTimeoutError
from .exceptions import StatusError
from .region import Region

Content = Union[Dict[str, Union[str, int, bytes]], bytes]


class Client:
    """Http client.

    :param username: PythonAnywhere username.
    :param token: API token.
    :param region: Account region.
    :param timeout: Request timeout.
    """

    __slots__ = (
        "_url",
        "_headers",
        "_timeout",
    )

    def __init__(
        self,
        username: str,
        token: str,
        region: Region,
        timeout: float,
    ) -> None:
        self._url = "https://{}.pythonanywhere.com/api/v0/user/{}".format(
            "eu" if region is Region.EU else "www", username
        )
        self._headers = {"Authorization": f"Token {token}"}
        self._timeout = timeout

    def _request(
        self,
        method: str,
        path: str,
        *,
        data: Optional[Dict[str, Optional[Union[str, int]]]] = None,
        params: Optional[Dict[str, Optional[Union[str, int]]]] = None,
        files: Optional[Dict[str, bytes]] = None,
    ) -> Response:
        try:
            response = requests.request(
                method=method,
                url=f"{self._url}/{path}",
                params=params,
                data=data,
                files=files,
                headers=self._headers,
                timeout=self._timeout,
            )
        except requests.Timeout:
            raise RequestTimeoutError(
                f"Request timed out (timeout={self._timeout})"
            ) from None

        if response.status_code >= 300:
            self._raise_for_status(response)

        return self._parse_content(response)

    def _raise_for_status(self, response: requests.Response) -> None:
        try:
            json = response.json()
        except requests.JSONDecodeError:
            json = {}

        status_code = response.status_code
        details = {
            "status_code": status_code,
            "description": json.get("error") or json.get("detail"),
            "raw_content": response.content,
        }

        if status_code == 400:
            raise BadRequestError(**details)
        elif status_code == 401:
            raise InvalidTokenError(**details)
        elif status_code == 401:
            raise InvalidTokenError(**details)
        elif status_code == 403:
            raise PermissionDeniedError(**details)
        elif status_code == 404:
            raise NotFoundError(**details)
        else:
            raise StatusError(**details)

    def _parse_content(self, response: requests.Response) -> Response:
        content: Optional[Content] = None
        content_type = response.headers.get("Content-Type", None)
        if response.content and content_type is not None:
            # response from /webapps with "text/json" in Content-Type
            if "/json" in content_type:  # json
                try:
                    content = response.json()
                except requests.JSONDecodeError:
                    raise InvalidJSONError(
                        f"Got invalid json: {response.content!r}"
                    ) from None
            elif "application/octet-stream" in content_type:  # file
                content = response.content
        return Response(status=response.status_code, content=content)

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Optional[Union[str, int]]]] = None,
    ) -> Response:
        return self._request("get", path, params=params)

    def post(
        self,
        path: str,
        *,
        data: Optional[Dict[str, Optional[Union[str, int]]]] = None,
        files: Optional[Dict[str, bytes]] = None,
    ) -> Response:
        return self._request("post", path, data=data, files=files)

    def patch(
        self,
        path: str,
        data: Optional[Dict[str, Optional[Union[str, int]]]] = None,
    ) -> Response:
        return self._request("patch", path, data=data)

    def delete(
        self,
        path: str,
        params: Optional[Dict[str, Optional[Union[str, int]]]] = None,
    ) -> Response:
        return self._request("delete", path, params=params)


@dataclass(frozen=True)
class Response:
    status: int
    content: Optional[Content] = None
