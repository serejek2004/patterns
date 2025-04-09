from dataclasses import dataclass


@dataclass
class TechnicalSpecialistDTO:
    manager_id: int

    @classmethod
    def from_request(cls, data):
        return cls(
            manager_id=data['manager_id']
        )
