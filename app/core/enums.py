from enum import Enum


class TaskStatus(str, Enum):
    INCOMPLETE = "INCOMPLETE"
    COMPLETE = "COMPLETE"
