from app import app, db
from flask import request, jsonify
from app.technical_specialist.service import TechnicalSpecialistService
from app.person.dto import PersonDTO
from app.person.service import PersonService
from app.employee.service import EmployeeService
from app.employee.dto import EmployeeDTO
from app.technical_specialist.dto import TechnicalSpecialistDTO

TechnicalSpecialistService = TechnicalSpecialistService(db)
EmployeeService = EmployeeService(db)
PersonService = PersonService(db)


@app.route('/technical_specialist', methods=['POST'])
def create_technical_specialist():
    data = request.get_json()

    person_dto = PersonDTO.from_request(data=data['employee']['person'])
    response, status_code = PersonService.create_person(person_dto=person_dto)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    employee_dto = EmployeeDTO.from_request(data=data['employee'])
    response, status_code = EmployeeService.create_employee(employee_dto=employee_dto, id=response)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    technical_specialist_dto = TechnicalSpecialistDTO.from_request(data=data)
    response, status_code = TechnicalSpecialistService.create_technical_specialist(id=response,
                                                                                   ts_dto=technical_specialist_dto)

    if status_code != 201:
        return jsonify({"message": "Failed to create customer"}), status_code

    return jsonify(response), 201


@app.route('/technical_specialist', methods=['GET'])
def get_all_technical_specialists():
    response, status_code = TechnicalSpecialistService.get_all()

    return jsonify(response), status_code


@app.route('/technical_specialist/<int:id>', methods=['GET'])
def get_technical_specialist_by_id(id: int):
    response, status_code = TechnicalSpecialistService.get_technical_specialist_by_id(id=id)

    return jsonify(response), status_code


@app.route('/technical_specialist/<int:id>', methods=['DELETE'])
def delete_technical_specialist_by_id(id: int):
    response, status_code = TechnicalSpecialistService.delete_technical_specialist_by_id(id=id)

    return jsonify({"message": response}), status_code


@app.route('/technical_specialist/<int:id>', methods=['PUT'])
def update_technical_specialist_by_id(id: int):
    data = request.get_json()
    data['person_id'] = id

    person_dto = PersonDTO.from_request(data['employee']['person'])
    response, status_code = PersonService.update_person(person_dto=person_dto, id=id)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    employee_dto = EmployeeDTO.from_request(data['employee'])
    response, status_code = EmployeeService.update_employee_by_id(id=id, employee_dto=employee_dto)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    response, status_code = TechnicalSpecialistService.update_technical_specialist_by_id(id=id)

    return jsonify(response), status_code
