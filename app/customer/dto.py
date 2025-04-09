from decimal import Decimal
from dataclasses import dataclass


@dataclass
class CustomerDTO:
    budget: Decimal

    @classmethod
    def from_request(cls, data: dict):
        return cls(
            budget=Decimal(data['budget']),
        )

