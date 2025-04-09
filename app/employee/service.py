from flask_sqlalchemy import SQLAlchemy
from app.employee.dao import EmployeeDAO
from app.models.models import Employee
from app.employee.dto import EmployeeDTO


class EmployeeService:
    def __init__(self, db: SQLAlchemy):
        self.dao = EmployeeDAO(db)

    def register_employee(self, employee_dto: EmployeeDTO, id: int) -> tuple[int, int]:
        new_employee = Employee(id=id, salary=employee_dto.salary)
        registered_employee = self.dao.register(model=new_employee)
        return registered_employee.id, 201

    def get_all(self) -> tuple[list, int]:
        return [employee.to_dict() for employee in self.dao.get_all(Employee)], 200

    def get_employee_by_id(self, id: int) -> tuple[dict, int] | tuple[None, int]:
        employee = self.dao.get(Employee, id)
        if not employee:
            return None, 404
        return employee.to_dict(), 200

    def delete_employee_by_id(self, id: int) -> tuple[str, int]:
        self.dao.delete(Employee, id)
        return "User deleted successfully", 204

    def update_employee_by_id(self, id: int, employee_dto: EmployeeDTO) -> tuple[dict, int]:
        updated_employee = self.dao.update(
            model=Employee,
            new_object=Employee(salary=employee_dto.salary),
            object_id=id
        )
        return updated_employee.to_dict(), 200
