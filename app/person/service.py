from flask_sqlalchemy import SQLAlchemy
from app.person.dao import PersonDAO
from app.models.models import Person
from app.core.email_validation import is_valid_email
from app.person.dto import PersonDTO


class PersonService:
    def __init__(self, db: SQLAlchemy):
        self.dao = PersonDAO(db)

    def register_person(self, person_dto: PersonDTO) -> tuple[str, int] | tuple[int, int]:
        if not is_valid_email(person_dto.email):
            return "Invalid email", 400

        if len(person_dto.name) > 32:
            return "Too long name", 400

        if len(person_dto.email) > 100:
            return "Too long email", 400

        if len(person_dto.phone_number) > 13:
            return "Too long phone number", 400

        registered_person = self.dao.register(model=Person(
            name=person_dto.name,
            email=person_dto.email,
            phone_number=person_dto.phone_number)
        )

        return registered_person.id, 201

    def update_person(self, person_dto: PersonDTO, id: int) -> tuple[str, int]:
        if not is_valid_email(person_dto.email):
            return "Invalid email", 400

        if len(person_dto.name) > 32:
            return "Too long name", 400

        if len(person_dto.email) > 100:
            return "Too long email", 400

        if len(person_dto.phone_number) > 32:
            return "Too long phone number", 400

        if not self.dao.get(model=Person, object_id=id):
            return "Person is not found", 404

        self.dao.update(model=Person,
                        new_object=Person(name=person_dto.name,
                                          email=person_dto.email,
                                          phone_number=person_dto.phone_number),
                        object_id=id)

        return "Person update successfully", 200
