from flask_sqlalchemy import SQLAlchemy
from app.task.dao import TaskDAO
from app.models.models import Task
from app.task.dto import TaskDTO


class TaskService:
    def __init__(self, db: SQLAlchemy):
        self.dao = TaskDAO(db)

    def create_task(self, task_dto: TaskDTO) -> tuple[dict | None, int]:
        new_task = Task(status=task_dto.status,
                        deadline=task_dto.deadline,
                        project_id=task_dto.project_id,
                        doer_id=task_dto.doer_id)
        created_task = self.dao.create(new_task)
        return created_task.to_dict(), 201

    def get_all(self) -> tuple[list, int]:
        return [project.to_dict() for project in self.dao.get_all(Task)], 200

    def get_task_by_id(self, id: int) -> tuple[dict, int] | tuple[None, int]:
        task = self.dao.get(Task, id)
        if not task:
            return None, 404
        return task.to_dict(), 200

    def delete_task_by_id(self, id: int) -> tuple[str, int]:
        self.dao.delete(Task, id)
        return "Task deleted successfully", 204

    def update_task_by_id(self, id: int, task_dto: TaskDTO) -> tuple[dict, int]:
        updated_task = self.dao.update(
            model=Task,
            new_object=Task(status=task_dto.status,
                            deadline=task_dto.deadline,
                            project_id=task_dto.project_id,
                            doer_id=task_dto.doer_id),
            object_id=id
        )
        return updated_task.to_dict(), 200
