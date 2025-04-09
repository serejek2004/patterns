from enum import Enum


class StatusEnum(Enum):
    IN_PROGRESS = "in_progress"
    NOT_STARTED = "not_started"
    DONE = "done"
    PAUSED = "paused"
