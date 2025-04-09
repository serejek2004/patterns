from flask_sqlalchemy import SQLAlchemy
from app.project.dao import ProjectDAO
from app.models.models import Project
from app.project.dto import ProjectDTO


class ProjectService:
    def __init__(self, db: SQLAlchemy):
        self.dao = ProjectDAO(db)

    def register_project(self, project_dto: ProjectDTO) -> tuple[dict | None, int]:
        new_project = Project(project_name=project_dto.project_name,
                              budget=project_dto.budget,
                              status=project_dto.status,
                              start_date=project_dto.start_date,
                              end_date=project_dto.end_date,
                              project_manager_id=project_dto.project_manager_id,
                              customer_id=project_dto.customer_id)
        registered_project = self.dao.register(new_project)
        return registered_project.to_dict(), 201

    def get_all(self) -> tuple[list, int]:
        return [project.to_dict() for project in self.dao.get_all(Project)], 200

    def get_project_by_id(self, id: int) -> tuple[dict, int] | tuple[None, int]:
        project = self.dao.get(Project, id)
        if not project:
            return None, 404
        return project.to_dict(), 200

    def delete_project_by_id(self, id: int) -> tuple[str, int]:
        self.dao.delete(Project, id)
        return "Project deleted successfully", 204

    def update_project_by_id(self, id: int, project_dto: ProjectDTO) -> tuple[dict, int]:
        updated_project = self.dao.update(
            model=Project,
            new_object=Project(project_name=project_dto.project_name,
                               budget=project_dto.budget,
                               status=project_dto.status,
                               start_date=project_dto.start_date,
                               end_date=project_dto.end_date,
                               project_manager_id=project_dto.project_manager_id,
                               customer_id=project_dto.customer_id),
            object_id=id
        )
        return updated_project.to_dict(), 200
