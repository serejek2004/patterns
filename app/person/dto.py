from dataclasses import dataclass


@dataclass
class PersonDTO:
    name: str
    phone_number: str
    email: str

    @classmethod
    def from_request(cls, data: dict):
        return cls(
            name=data['name'],
            phone_number=data['phone_number'],
            email=data['email'],
        )
