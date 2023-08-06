from __future__ import annotations

__all__ = [
    "ScheduledTask",
    "AlwaysOnTask",
]

from typing import List
from typing import Optional
from typing import Union
from typing import cast

from pawapi.interval import TaskInterval

from ._types import Content
from .base import BaseEndpoint


class ScheduledTask(BaseEndpoint):
    """Scheduled task endpoint"""

    __path = "schedule"

    __slots__ = ()

    def list(self) -> List[Content]:
        """List all tasks."""

        result = self._client.get(f"{self.__path}/")
        return cast(List[Content], result.content)

    def create(
        self,
        command: str,
        minute: Union[int, str],
        *,
        hour: Optional[Union[int, str]] = None,
        enabled: bool = True,
        interval: TaskInterval = TaskInterval.DAILY,
        description: Optional[str] = None,
    ) -> Content:
        """Create a new task.

        :param command: Command to execute.
        :param minute: Start time (hourly task).
        :param hour: Start time (daily task).
        :param enabled: Enable task.
        :param interval: Task start interval.
        :param description: Task description.
        :returns: Task information.
        """

        result = self._client.post(
            path=f"{self.__path}/",
            data={
                "command": command,
                "enabled": enabled,
                "interval": interval.value,
                "hour": hour,
                "minute": minute,
                "description": description,
            },
        )
        return cast(Content, result.content)

    def get_info(self, task_id: Union[int, str]) -> Content:
        """Returns information about task.

        :param task_id: Task id.
        """

        result = self._client.get(f"{self.__path}/{task_id}/")
        return cast(Content, result.content)

    def update(
        self,
        task_id: Union[int, str],
        *,
        command: Optional[str] = None,
        enabled: Optional[bool] = None,
        interval: Optional[TaskInterval] = None,
        hour: Optional[Union[int, str]] = None,
        minute: Optional[Union[int, str]] = None,
        description: Optional[str] = None,
    ) -> Content:
        """Update task.

        :param task_id: Task id.
        :param command: Command to execute.
        :param minute: Start time (hourly task).
        :param hour: Start time (daily task).
        :param enabled: Enable task.
        :param interval: Task start interval.
        :param description: Task description.
        :returns: Task information.
        """

        result = self._client.patch(
            path=f"{self.__path}/{task_id}/",
            data={
                "command": command,
                "enabled": enabled,
                "interval": interval.value if interval is not None else None,
                "hour": hour,
                "minute": minute,
                "description": description,
            },
        )
        return cast(Content, result.content)

    def delete(self, task_id: Union[int, str]) -> bool:
        """Stop and delete task.

        :param task_id: Task id.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/{task_id}/")
        return result.status == 204


class AlwaysOnTask(BaseEndpoint):
    """Always-on task endpoint"""

    __path = "always_on"

    __slots__ = ()

    def list(self) -> List[Content]:
        """List all tasks."""

        result = self._client.get(f"{self.__path}/")
        return cast(List[Content], result.content)

    def create(
        self,
        command: str,
        *,
        enabled: bool = True,
        description: Optional[str] = None,
    ) -> Content:
        """Create a new task.

        :param command: Command to execute.
        :param enabled: Enable task.
        :param description: Task description.
        :returns: Task information.
        """

        result = self._client.post(
            path=f"{self.__path}/",
            data={
                "command": command,
                "description": description,
                "enabled": enabled,
            },
        )
        return cast(Content, result.content)

    def get_info(self, task_id: Union[int, str]) -> Content:
        """Returns information about task."""

        result = self._client.get(f"{self.__path}/{task_id}/")
        return cast(Content, result.content)

    def update(
        self,
        task_id: Union[int, str],
        *,
        command: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> Content:
        """Update task.

        :param task_id: Task id.
        :param command: Command to execute.
        :param enabled: Enable task.
        :param description: Task description.
        :returns: Task information.
        """

        result = self._client.patch(
            path=f"{self.__path}/{task_id}/",
            data={
                "command": command,
                "description": description,
                "enabled": enabled,
            },
        )
        return cast(Content, result.content)

    def delete(self, task_id: Union[int, str]) -> bool:
        """Stop and delete task.

        :param task_id: Task id.
        :returns: True on success.
        """

        result = self._client.delete(f"{self.__path}/{task_id}/")
        return result.status == 204

    def restart(
        self,
        task_id: Union[int, str],
        *,
        command: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> Content:
        """Restart task.

        :param task_id: Task id.
        :param command: Command to execute.
        :param enabled: Enable task.
        :param description: Task description.
        :returns: Task information
        """

        result = self._client.post(
            path=f"{self.__path}/{task_id}/restart/",
            data={
                "command": command,
                "description": description,
                "enabled": enabled,
            },
        )
        return cast(Content, result.content)
