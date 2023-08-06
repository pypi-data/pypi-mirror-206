from __future__ import annotations

__all__ = ["Webapp"]

from typing import TYPE_CHECKING
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from typing import cast

from pawapi.exceptions import BadRequestError
from pawapi.exceptions import StatusError

from ._types import Content
from .base import BaseEndpoint

if TYPE_CHECKING:  # pragma: no cover
    from pawapi.python import Python2
    from pawapi.python import Python3


class Webapp(BaseEndpoint):
    """Web app endpoint"""

    __path = "webapps"

    __slots__ = ()

    def list(self) -> List[Content]:
        """List all webapps."""

        result = self._client.get(f"{self.__path}/")
        return cast(List[Content], result.content)

    def create(
        self,
        domain_name: str,
        python_version: Union[Python2, Python3],
    ) -> bool:
        """Create a new webapp.

        .. note::

            Use :meth:`update` to modify configuration.

        :param domain_name: App domain name.
        :param python_version: App Python version.
        :returns: True on success.
        """

        result = self._client.post(
            path="webapps/",
            data={
                "domain_name": domain_name,
                "python_version": python_version.format_value(dot=False),
            },
        )
        return result.status == 200

    def get_info(self, domain_name: str) -> Content:
        """Returns app configuration.

        :param domain_name: App domain name.
        """

        result = self._client.get(f"{self.__path}/{domain_name}/")
        return cast(Content, result.content)

    def update(
        self,
        domain_name: str,
        *,
        python_version: Optional[Union[Python2, Python3]] = None,
        source_directory: Optional[str] = None,
        virtualenv_path: Optional[str] = None,
        force_https: Optional[bool] = None,
        protection: Optional[bool] = None,
        protection_username: Optional[str] = None,
        protection_password: Optional[str] = None,
    ) -> Content:
        """Modify app configuration.

        .. note::

            Restart the webapp is required to apply the changes.

        :param domain_name: App domain name.
        :param python_version: App Python version.
        :param source_directory: Path to app source directory.
        :param virtualenv_path: Path to app virtualenv.
        :param force_https: Redirect http to https.
        :param protection: Use password protection.
        :param protection_username: Username for password protection.
        :param protection_password: Password for password protection.
        :returns: App configuration.
        """

        pyver = None
        if python_version is not None:
            pyver = python_version.format_value(short=True)

        result = self._client.patch(
            path=f"{self.__path}/{domain_name}/",
            data={
                "python_version": pyver,
                "source_directory": source_directory,
                "virtualenv_path": virtualenv_path,
                "force_https": force_https,
                "password_protection_enabled": protection,
                "password_protection_username": protection_username,
                "password_protection_password": protection_password,
            },
        )
        return cast(Content, result.content)

    def delete(self, domain_name: str) -> bool:
        """Delete the webapp.

        .. note::

            Config is backed up in /var/www, and your code is not touched.

        :param domain_name: App domain name.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/{domain_name}/")
        return result.status == 204

    def enable(self, domain_name: str) -> bool:
        """Enable the webapp.

        :param domain_name: App domain name.
        :returns: True on success.
        """

        try:
            result = self._client.post(f"{self.__path}/{domain_name}/enable/")
        # returns 400 if you try to enable an already enabled app
        except BadRequestError as error:
            if error.description is not None:
                if "cannot create any more webapps" in error.description:
                    return True
            raise  # pragma: no cover

        content = cast(Dict[str, str], result.content)
        return content["status"] == "OK"

    def disable(self, domain_name: str) -> bool:
        """Disable the webapp.

        :param domain_name: App domain name.
        :returns: True on success.
        """

        result = self._client.post(f"{self.__path}/{domain_name}/disable/")
        content = cast(Dict[str, str], result.content)
        return content["status"] == "OK"

    def reload(self, domain_name: str) -> bool:
        """Reload the webapp.

        :param domain_name: App domain name.
        :returns: True on success.
        """

        try:
            result = self._client.post(f"{self.__path}/{domain_name}/reload/")
        # returns status 500 if you try to reload disabled app
        except StatusError:
            return False

        content = cast(Dict[str, str], result.content)
        return content["status"] == "OK"

    def get_ssl_info(self, domain_name: str) -> Content:
        """Returns info about app's certificate.

        :param domain_name: App domain name.
        """

        result = self._client.get(f"{self.__path}/{domain_name}/ssl/")
        return cast(Content, result.content)

    def add_ssl(
        self,
        domain_name: str,
        cert: str,
        private_key: str,
    ) -> bool:
        """Set new certificate.

        :param domain_name: App domain name.
        :param cert: Certificate.
        :param private_key: Certificate private key.
        :returns: True on success.
        """

        result = self._client.post(
            path=f"{self.__path}/{domain_name}/ssl/",
            data={
                "cert": cert,
                "private_key": private_key,
            },
        )
        content = cast(Dict[str, str], result.content)
        return content["status"] == "OK"

    def delete_ssl(self, domain_name: str) -> bool:
        """Delete webapp's SSL.

        :param domain_name: App domain name.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/{domain_name}/ssl/")
        content = cast(Dict[str, str], result.content)
        return content["status"] == "OK"

    def list_static_files(self, domain_name: str) -> List[Content]:
        """List all the static file mappings for a domain.

        :param domain_name: App domain name.
        """

        result = self._client.get(f"{self.__path}/{domain_name}/static_files/")
        return cast(List[Content], result.content)

    def add_static_file(
        self,
        domain_name: str,
        url: str,
        path: str,
    ) -> Content:
        """Create a new static files mapping.

        .. note::

            Webapp restart required.

        :param domain_name: App domain name.
        :param url: Static files URL.
        :param path: Path to static files directory.
        """

        result = self._client.post(
            path=f"{self.__path}/{domain_name}/static_files/",
            data={
                "url": url,
                "path": path,
            },
        )
        return cast(Content, result.content)

    def get_static_file_info(
        self,
        domain_name: str,
        file_id: int,
    ) -> Content:
        """Get static files info.

        URL and path of a particular mapping.

        :param domain_name: App domain name.
        :param file_id: Static files id (see `Webapp.list_static_files()`).
        """

        result = self._client.get(
            f"{self.__path}/{domain_name}/static_files/{file_id}/"
        )
        return cast(Content, result.content)

    def update_static_file(
        self,
        domain_name: str,
        file_id: int,
        url: str,
        path: str,
    ) -> Content:
        """Modify a static files mapping.

        .. note::

            Webapp restart required.

        :param domain_name: App domain name.
        :param file_id: Static files id.
        :param url: Static files URL.
        :param path: Path to static files directory.
        """

        result = self._client.patch(
            path=f"{self.__path}/{domain_name}/static_files/{file_id}/",
            data={
                "url": url,
                "path": path,
            },
        )
        return cast(Content, result.content)

    def delete_static_file(self, domain_name: str, file_id: int) -> bool:
        """Remove a static files mapping.

        .. note::

            Webapp restart required.

        :param domain_name: App domain name.
        :param file_id: Static files id.
        :returns: True on success.
        """

        result = self._client.delete(
            f"{self.__path}/{domain_name}/static_files/{file_id}/"
        )
        return result.status == 204

    def list_static_headers(self, domain_name: str) -> List[Content]:
        """List all the static headers for a domain.

        :param domain_name: App domain name.
        """

        result = self._client.get(
            f"{self.__path}/{domain_name}/static_headers/"
        )
        return cast(List[Content], result.content)

    def add_static_header(
        self,
        domain_name: str,
        url: str,
        name: str,
        value: str,
    ) -> Content:
        """Create a new static header.

        .. note::

            Webapp restart required.

        :param domain_name: App domain name.
        :param url: Header url.
        :param name: Header name.
        :param value: Header value.
        """

        result = self._client.post(
            path=f"{self.__path}/{domain_name}/static_headers/",
            data={
                "url": url,
                "name": name,
                "value": value,
            },
        )
        return cast(Content, result.content)

    def get_static_header_info(
        self,
        domain_name: str,
        header_id: int,
    ) -> Content:
        """Get header info.

        :param domain_name: App domain name.
        :param header_id: Header id.
        """

        result = self._client.get(
            f"{self.__path}/{domain_name}/static_headers/{header_id}/"
        )
        return cast(Content, result.content)

    def update_static_header(
        self,
        domain_name: str,
        header_id: int,
        url: str,
        name: str,
        value: str,
    ) -> Content:
        """Modify a static header.

        .. note::

            Webapp restart required.

        :param domain_name: App domain name.
        :param header_id: Header id.
        :param url: Header url.
        :param name: Header name.
        :param value: Header value.
        """

        result = self._client.patch(
            path=f"{self.__path}/{domain_name}/static_headers/{header_id}/",
            data={
                "url": url,
                "name": name,
                "value": value,
            },
        )
        return cast(Content, result.content)

    def delete_static_header(
        self,
        domain_name: str,
        header_id: int,
    ) -> bool:
        """Remove a static header.

        .. note::

            Webapp restart required.

        :param domain_name: App domain name.
        :param header_id: Header id.
        :returns: True on success.
        """

        result = self._client.delete(
            f"{self.__path}/{domain_name}/static_headers/{header_id}/"
        )
        return result.status == 204
