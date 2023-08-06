from enum import Enum


class TaskInterval(Enum):
    """Task start interval.

    See :meth:`pawapi.api.ScheduledTask.create()`.
    """

    DAILY = "daily"
    HOURLY = "hourly"
