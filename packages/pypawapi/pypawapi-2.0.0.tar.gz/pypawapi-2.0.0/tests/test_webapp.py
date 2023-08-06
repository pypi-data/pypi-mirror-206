from typing import TYPE_CHECKING
from typing import Dict
from typing import Union

import pytest
from responses.matchers import urlencoded_params_matcher

from pawapi.exceptions import BadRequestError
from pawapi.python import Python3

if TYPE_CHECKING:
    from responses import RequestsMock


@pytest.fixture
def params_static_files() -> Dict[str, str]:
    return {
        "url": "/static",
        "path": "/home/user/static",
    }


@pytest.fixture
def params_static_headers() -> Dict[str, str]:
    return {
        "url": "/header",
        "name": "headername",
        "value": "headervalue",
    }


@pytest.fixture(params=(55, "55"))
def file_id(request: pytest.FixtureRequest) -> Union[int, str]:
    return request.param


@pytest.fixture(params=(44, "44"))
def header_id(request: pytest.FixtureRequest) -> Union[int, str]:
    return request.param


@pytest.mark.usefixtures("paw_api_client")
class TestWebApp:
    domain = "test.domain.site"
    file_id = 321
    header_id = 123

    def test_list(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(f"{self.url}/webapps/")
        self.api.webapp.list()

    def test_create(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.post(
            url=f"{self.url}/webapps/",
            match=(
                urlencoded_params_matcher({
                    "domain_name": self.domain,
                    "python_version": "python38",
                }),
            ),
        )
        assert self.api.webapp.create(
            domain_name=self.domain,
            python_version=Python3.PYTHON38,
        )

    def test_info(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(f"{self.url}/webapps/{self.domain}/", json={})
        res = self.api.webapp.get_info(self.domain)
        assert isinstance(res, dict), res

    def test_update(self, mock_responses: 'RequestsMock') -> None:
        params = {
            "source_directory": "/home/user/appsrc",
            "virtualenv_path": "/home/user/venv",
            "force_https": True,
        }
        mock_responses.patch(
            url=f"{self.url}/webapps/{self.domain}/",
            match=(
                urlencoded_params_matcher({
                    "python_version": "3.9",
                    **{k: str(v)
                       for k, v in params.items()}
                }),
            ),
            json={},
        )
        res = self.api.webapp.update(
            domain_name=self.domain,
            python_version=Python3.PYTHON39,
            **params,
        )
        assert isinstance(res, dict), res

    def test_update_protected(self, mock_responses: 'RequestsMock') -> None:
        user = "username"
        pwd = "password123"

        mock_responses.patch(
            url=f"{self.url}/webapps/{self.domain}/",
            match=(
                urlencoded_params_matcher({
                    "password_protection_enabled": "True",
                    "password_protection_username": user,
                    "password_protection_password": pwd,
                }),
            ),
            json={},
        )
        res = self.api.webapp.update(
            domain_name=self.domain,
            protection=True,
            protection_username=user,
            protection_password=pwd,
        )
        assert isinstance(res, dict), res

    def test_delete(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.delete(f"{self.url}/webapps/{self.domain}/", status=204)
        assert self.api.webapp.delete(self.domain)

    def test_enable(self, mock_responses: 'RequestsMock') -> None:
        json = {"status": "OK"}
        mock_responses.post(
            f"{self.url}/webapps/{self.domain}/enable/", json=json
        )
        assert self.api.webapp.enable(self.domain)

    def test_enable_enabled(self, mock_responses: 'RequestsMock') -> None:
        json = {"error": "You cannot create any more webapps - ..."}
        mock_responses.post(
            f"{self.url}/webapps/{self.domain}/enable/",
            json=json,
            status=400,
        )
        assert self.api.webapp.enable(self.domain)

    def test_disable(self, mock_responses: 'RequestsMock') -> None:
        json = {"status": "OK"}
        mock_responses.post(
            f"{self.url}/webapps/{self.domain}/disable/", json=json
        )
        assert self.api.webapp.disable(self.domain)

    def test_reload(self, mock_responses: 'RequestsMock') -> None:
        json = {"status": "OK"}
        mock_responses.post(
            f"{self.url}/webapps/{self.domain}/reload/", json=json
        )
        assert self.api.webapp.reload(self.domain)

    def test_reload_disabled(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.post(
            f"{self.url}/webapps/{self.domain}/reload/",
            status=500,
        )
        assert not self.api.webapp.reload(self.domain)

    def test_ssl_info(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(f"{self.url}/webapps/{self.domain}/ssl/", json={})
        res = self.api.webapp.get_ssl_info(self.domain)
        assert isinstance(res, dict), res

    def test_add_ssl(self, mock_responses: 'RequestsMock') -> None:
        params = {
            "cert": "cert",
            "private_key": "privete_key",
        }
        mock_responses.post(
            url=f"{self.url}/webapps/{self.domain}/ssl/",
            match=(urlencoded_params_matcher(params), ),
            json={"status": "OK"},
        )
        assert self.api.webapp.add_ssl(domain_name=self.domain, **params)

    def test_add_ssl_invalid_cred(self, mock_responses: 'RequestsMock') -> None:
        params = {
            "cert": "cert",
            "private_key": "privete_key",
        }
        mock_responses.post(
            url=f"{self.url}/webapps/{self.domain}/ssl/",
            match=(urlencoded_params_matcher(params), ),
            status=400,
        )
        with pytest.raises(BadRequestError):
            self.api.webapp.add_ssl(domain_name=self.domain, **params)

    def test_delete_ssl(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.delete(
            f"{self.url}/webapps/{self.domain}/ssl/",
            json={"status": "OK"},
        )
        assert self.api.webapp.delete_ssl(self.domain)

    def test_list_static_files(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(
            f"{self.url}/webapps/{self.domain}/static_files/",
            body=b"[]",
            content_type="application/json",
        )
        res = self.api.webapp.list_static_files(self.domain)
        assert isinstance(res, list)

    def test_add_static_file(
        self,
        mock_responses: 'RequestsMock',
        params_static_files: Dict[str, str],
    ) -> None:
        mock_responses.post(
            url=f"{self.url}/webapps/{self.domain}/static_files/",
            match=(urlencoded_params_matcher(params_static_files), ),
            json={},
        )
        res = self.api.webapp.add_static_file(
            domain_name=self.domain,
            **params_static_files,
        )
        assert isinstance(res, dict)

    def test_static_file_info(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(
            f"{self.url}/webapps/{self.domain}/static_files/{self.file_id}/",
            json={},
        )
        res = self.api.webapp.get_static_file_info(self.domain, self.file_id)
        assert isinstance(res, dict)

    def test_update_static_file(
        self,
        mock_responses: 'RequestsMock',
        params_static_files: Dict[str, str],
    ) -> None:
        mock_responses.patch(
            url=f"{self.url}/webapps/{self.domain}/static_files/{self.file_id}/",  # noqa: E501
            match=(urlencoded_params_matcher(params_static_files), ),
            json={},
        )  # yapf: disable
        res = self.api.webapp.update_static_file(
            domain_name=self.domain,
            file_id=self.file_id,
            **params_static_files,
        )
        assert isinstance(res, dict)

    def test_delete_static_file(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.delete(
            f"{self.url}/webapps/{self.domain}/static_files/{self.file_id}/",
            status=204,
        )
        assert self.api.webapp.delete_static_file(self.domain, self.file_id)

    def test_list_static_headers(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(
            f"{self.url}/webapps/{self.domain}/static_headers/",
            content_type="application/json",
            body=b"[]",
        )
        res = self.api.webapp.list_static_headers(self.domain)
        assert isinstance(res, list)

    def test_add_static_header(
        self,
        mock_responses: 'RequestsMock',
        params_static_headers: Dict[str, str]
    ) -> None:
        mock_responses.post(
            url=f"{self.url}/webapps/{self.domain}/static_headers/",
            match=(urlencoded_params_matcher(params_static_headers), ),
            json={},
        )
        res = self.api.webapp.add_static_header(
            domain_name=self.domain,
            **params_static_headers,
        )
        assert isinstance(res, dict)

    def test_static_header_info(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(
            f"{self.url}/webapps/{self.domain}/static_headers/{self.header_id}/",  # noqa: E501
            json={},
        )
        res = self.api.webapp.get_static_header_info(
            self.domain,
            self.header_id,
        )
        assert isinstance(res, dict)

    def test_update_static_header(
        self,
        mock_responses: 'RequestsMock',
        params_static_headers: Dict[str, str],
    ) -> None:
        mock_responses.patch(
            url=f"{self.url}/webapps/{self.domain}/static_headers/{self.header_id}/",  # noqa: E501
            match=(urlencoded_params_matcher(params_static_headers), ),
            json={},
        )  # yapf: disable
        res = self.api.webapp.update_static_header(
            domain_name=self.domain,
            header_id=self.header_id,
            **params_static_headers,
        )
        assert isinstance(res, dict)

    def test_delete_static_header(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.delete(
            f"{self.url}/webapps/{self.domain}/static_headers/{self.header_id}/",  # noqa: E501
            status=204,
        )
        assert self.api.webapp.delete_static_header(self.domain, self.header_id)
