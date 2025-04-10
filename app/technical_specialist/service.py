from flask_sqlalchemy import SQLAlchemy
from app.technical_specialist.dao import TechnicalSpecialistDAO
from app.models.models import TechnicalSpecialist
from app.technical_specialist.dto import TechnicalSpecialistDTO


class TechnicalSpecialistService:
    def __init__(self, db: SQLAlchemy):
        self.dao = TechnicalSpecialistDAO(db)

    def create_technical_specialist(self, id: int, ts_dto: TechnicalSpecialistDTO) -> tuple[dict | None, int]:
        new_technical_specialist = TechnicalSpecialist(id=id, manager_id=ts_dto.manager_id)
        registered_technical_specialist = self.dao.create(new_technical_specialist)
        return registered_technical_specialist.to_dict(), 201

    def get_all(self) -> tuple[list, int]:
        return [technical_specialist.to_dict() for technical_specialist in self.dao.get_all(TechnicalSpecialist)], 200

    def get_technical_specialist_by_id(self, id: int) -> tuple[dict, int] | tuple[None, int]:
        technical_specialist = self.dao.get(TechnicalSpecialist, id)
        if not technical_specialist:
            return None, 404
        return technical_specialist.to_dict(), 200

    def delete_technical_specialist_by_id(self, id: int) -> tuple[str, int]:
        self.dao.delete(TechnicalSpecialist, id)
        return "User deleted successfully", 204

    def update_technical_specialist_by_id(self, id: int) -> tuple[dict, int]:
        updated_technical_specialist = self.dao.update(
            model=TechnicalSpecialist,
            new_object=TechnicalSpecialist,
            object_id=id
        )
        return updated_technical_specialist.to_dict(), 200
