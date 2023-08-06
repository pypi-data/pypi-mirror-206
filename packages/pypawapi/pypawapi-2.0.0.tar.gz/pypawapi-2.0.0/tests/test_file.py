from typing import TYPE_CHECKING

import pytest
from responses.matchers import multipart_matcher
from responses.matchers import query_param_matcher
from responses.matchers import urlencoded_params_matcher

if TYPE_CHECKING:
    from responses import RequestsMock

FILE_PATH = "/home/user123/file.md"
DIR_PATH = "/home/user123/dir"


@pytest.mark.usefixtures("paw_api_client")
class TestFiles:

    def test_get_file_content(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(
            f"{self.url}/files/path{FILE_PATH}",
            body=b"foo",
            content_type="application/octet-stream",
        )
        res = self.api.file.get_file_content(FILE_PATH)
        assert res is not None, res

    def test_get_file_content_not_a_file(
        self, mock_responses: 'RequestsMock'
    ) -> None:
        mock_responses.get(
            f"{self.url}/files/path{FILE_PATH}",
            json={"foo": {}},
        )
        res = self.api.file.get_file_content(FILE_PATH)
        assert res is None, res

    def test_get_directory_content(
        self, mock_responses: 'RequestsMock'
    ) -> None:
        mock_responses.get(
            f"{self.url}/files/path{DIR_PATH}",
            json={
                "foo": {
                    "type": "file",
                    "url": "/foo",
                },
                "bar": {
                    "type": "directory",
                    "url": "/bar",
                },
            },
        )
        res = self.api.file.get_directory_content(DIR_PATH)
        assert res is not None, res

    def test_get_directory_content_not_a_dir(
        self, mock_responses: 'RequestsMock'
    ) -> None:
        mock_responses.get(
            f"{self.url}/files/path{DIR_PATH}",
            body=b"bar",
            content_type="application/octet-stream",
        )
        res = self.api.file.get_directory_content(DIR_PATH)
        assert res is None, res

    def test_upload_file_new(self, mock_responses: 'RequestsMock') -> None:
        content = b"file"
        mock_responses.post(
            url=f"{self.url}/files/path{FILE_PATH}",
            match=(multipart_matcher({"content": content}), ),
            status=201,
        )
        assert self.api.file.upload(path=FILE_PATH, file_content=content)

    def test_upload_file_update(self, mock_responses: 'RequestsMock') -> None:
        content = b"file"
        mock_responses.post(
            url=f"{self.url}/files/path{FILE_PATH}",
            match=(multipart_matcher({"content": content}), ),
            status=200,
        )
        assert not self.api.file.upload(path=FILE_PATH, file_content=content)

    def test_delete_file(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.delete(f"{self.url}/files/path{FILE_PATH}", status=204)
        assert self.api.file.delete(FILE_PATH)

    def test_start_sharing_file(self, mock_responses: 'RequestsMock') -> None:
        path = "/foo/bar/"
        mock_responses.post(
            url=f"{self.url}/files/sharing/",
            match=(urlencoded_params_matcher({"path": FILE_PATH}), ),
            json={"url": path},
        )
        res = self.api.file.start_sharing(path=FILE_PATH)
        assert res == path

    def test_get_sharing_status(self, mock_responses: 'RequestsMock') -> None:
        path = "/foo/bar/"
        mock_responses.get(
            url=f"{self.url}/files/sharing/",
            match=(query_param_matcher({"path": FILE_PATH}), ),
            json={"url": path},
        )
        res = self.api.file.get_sharing_status(path=FILE_PATH)
        assert res == path

    def test_get_sharing_status_none(
        self, mock_responses: 'RequestsMock'
    ) -> None:
        mock_responses.get(
            url=f"{self.url}/files/sharing/",
            match=(query_param_matcher({"path": FILE_PATH}), ),
            status=404
        )
        res = self.api.file.get_sharing_status(path=FILE_PATH)
        assert res is None

    def test_stop_sharing_file(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.delete(
            url=f"{self.url}/files/sharing/",
            match=(query_param_matcher({"path": FILE_PATH}), ),
            status=204,
        )
        assert self.api.file.stop_sharing(path=FILE_PATH)

    def test_get_tree(self, mock_responses: 'RequestsMock') -> None:
        path = "/home/user/"
        mock_responses.get(
            url=f"{self.url}/files/tree/",
            match=(query_param_matcher({"path": path}), ),
            content_type="application/json",
            body=b"[]",
        )
        res = self.api.file.get_tree(path=path)
        assert isinstance(res, list)

    def test_get_tree_not_found(self, mock_responses: 'RequestsMock') -> None:
        path = "/home/user/"
        mock_responses.get(
            url=f"{self.url}/files/tree/",
            match=(query_param_matcher({"path": path}), ),
            status=400,
        )
        res = self.api.file.get_tree(path=path)
        assert res is None
