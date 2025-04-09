from decimal import Decimal
from dataclasses import dataclass
from datetime import datetime
from app.core.status_enum import StatusEnum
from app.core.time_parse import datetime_parse


@dataclass
class ProjectDTO:
    project_name: str
    customer_id: int
    project_manager_id: int
    status: StatusEnum
    start_date: datetime
    end_date: datetime
    budget: Decimal

    @classmethod
    def from_request(cls, data: dict):
        return cls(
            project_name=data['project_name'],
            customer_id=data['customer_id'],
            project_manager_id=data['project_manager_id'],
            status=data['status'],
            start_date=datetime_parse(data['start_date']),
            end_date=datetime_parse(data['end_date']),
            budget=data['budget']
        )
