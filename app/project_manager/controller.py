from app import app, db
from flask import request, jsonify
from app.project_manager.service import ProjectManagerService
from app.person.dto import PersonDTO
from app.person.service import PersonService
from app.employee.service import EmployeeService
from app.employee.dto import EmployeeDTO

ProjectManagerService = ProjectManagerService(db)
EmployeeService = EmployeeService(db)
PersonService = PersonService(db)


@app.route('/project_manager', methods=['POST'])
def register_project_manager():
    data = request.get_json()

    person_dto = PersonDTO.from_request(data=data['employee']['person'])
    response, status_code = PersonService.register_person(person_dto=person_dto)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    employee_dto = EmployeeDTO.from_request(data['employee'])
    response, status_code = EmployeeService.register_employee(employee_dto=employee_dto, id=response)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    response, status_code = ProjectManagerService.register(id=response)

    if status_code != 201:
        return jsonify({"message": "Failed to create customer"}), status_code

    return jsonify(response), 201


@app.route('/project_manager', methods=['GET'])
def get_all_project_managers():
    response, status_code = ProjectManagerService.get_all()

    return jsonify(response), status_code


@app.route('/project_manager/<int:id>', methods=['GET'])
def get_project_manager_by_id(id: int):
    response, status_code = ProjectManagerService.get_project_manager_by_id(id=id)

    return jsonify(response), status_code


@app.route('/project_manager/<int:id>', methods=['DELETE'])
def delete_project_manager_by_id(id: int):
    response, status_code = ProjectManagerService.delete_project_manager_by_id(id=id)

    return jsonify({"message": response}), status_code


@app.route('/project_manager/<int:id>', methods=['PUT'])
def update_project_manager_by_id(id: int):
    data = request.get_json()

    person_dto = PersonDTO.from_request(data=data['employee']['person'])
    response, status_code = PersonService.update_person(person_dto=person_dto, id=id)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    employee_dto = EmployeeDTO.from_request(data=data['employee'])
    response, status_code = EmployeeService.update_employee_by_id(id=id, employee_dto=employee_dto)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    response, status_code = ProjectManagerService.update_project_manager_by_id(id=id)

    return jsonify(response), status_code
