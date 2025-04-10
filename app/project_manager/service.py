from flask_sqlalchemy import SQLAlchemy
from app.project_manager.dao import ProjectManagerDAO
from app.models.models import ProjectManager


class ProjectManagerService:
    def __init__(self, db: SQLAlchemy):
        self.dao = ProjectManagerDAO(db)

    def create_project_manager(self, id: int) -> tuple[dict | None, int]:
        new_project_manager = ProjectManager(id=id)
        registered_project_manager = self.dao.create(new_project_manager)
        return registered_project_manager.to_dict(), 201

    def get_all(self) -> tuple[list, int]:
        return [project_manager.to_dict() for project_manager in self.dao.get_all(ProjectManager)], 200

    def get_project_manager_by_id(self, id: int) -> tuple[dict, int] | tuple[None, int]:
        project_manager = self.dao.get(ProjectManager, id)
        if not project_manager:
            return None, 404
        return project_manager.to_dict(), 200

    def delete_project_manager_by_id(self, id: int) -> tuple[str, int]:
        self.dao.delete(ProjectManager, id)
        return "User deleted successfully", 204

    def update_project_manager_by_id(self, id: int) -> tuple[dict, int]:
        updated_project_manager = self.dao.update(
            model=ProjectManager,
            new_object=ProjectManager,
            object_id=id
        )
        return updated_project_manager.to_dict(), 200
