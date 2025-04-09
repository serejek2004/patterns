from decimal import Decimal
from dataclasses import dataclass


@dataclass
class EmployeeDTO:
    salary: Decimal

    @classmethod
    def from_request(cls, data):
        return cls(
            salary=Decimal(data['salary']),
        )
