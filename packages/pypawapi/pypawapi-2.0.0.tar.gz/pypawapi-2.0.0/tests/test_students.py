from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from responses import RequestsMock


@pytest.mark.usefixtures("paw_api_client")
class TestStudents:

    def test_list(self, mock_responses: 'RequestsMock') -> None:
        mock_responses.get(f"{self.url}/students/", json={})
        res = self.api.students.list()
        assert isinstance(res, list), res

    @pytest.mark.parametrize("student", ("student1", "anotherstudent2"))
    def test_delete(self, mock_responses: 'RequestsMock', student: str) -> None:
        mock_responses.delete(f"{self.url}/students/{student}/", status=204)
        assert self.api.students.delete(student)
