from dataclasses import dataclass
from datetime import datetime
from app.core.status_enum import StatusEnum
from app.core.time_parse import datetime_parse


@dataclass
class TaskDTO:
    status: StatusEnum
    deadline: datetime
    doer_id: int
    project_id: int

    @classmethod
    def from_request(cls, data: dict):
        return cls(
            doer_id=data['doer_id'],
            project_id=data['project_id'],
            status=data['status'],
            deadline=datetime_parse(data['deadline']),
        )
