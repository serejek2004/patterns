from app import app, db
from flask import request, jsonify
from app.customer.dto import CustomerDTO
from app.customer.service import CustomerService
from app.person.dto import PersonDTO
from app.person.service import PersonService

CustomerService = CustomerService(db)
PersonService = PersonService(db)


@app.route('/customer', methods=['POST'])
def create_customer():
    data = request.get_json()

    person_dto = PersonDTO.from_request(data=data['person'])
    response, status_code = PersonService.create_person(person_dto=person_dto)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    customer_dto = CustomerDTO.from_request(data=data)
    customer, status_code = CustomerService.create(customer_dto=customer_dto, id=response)

    if status_code != 201:
        return jsonify({"message": "Failed to create customer"}), status_code

    return jsonify(customer), 201


@app.route('/customer', methods=['GET'])
def get_all_customers():
    customers, status_code = CustomerService.get_all()

    return jsonify(customers), status_code


@app.route('/customer/<int:id>', methods=['GET'])
def get_customer_by_id(id: int):
    customer, status_code = CustomerService.get_customer_by_id(id=id)

    return jsonify(customer), status_code


@app.route('/customer/<int:id>', methods=['DELETE'])
def delete_customer_by_id(id: int):
    response, status_code = CustomerService.delete_customer_by_id(id=id)

    return jsonify({"message": response}), status_code


@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer_by_id(id: int):
    data = request.get_json()

    person_dto = PersonDTO.from_request(data=data['person'])
    response, status_code = PersonService.update_person(person_dto=person_dto, id=id)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    customer_dto = CustomerDTO.from_request(data=data)
    customer, status_code = CustomerService.update_customer_by_id(id=id, customer_dto=customer_dto)

    return jsonify(customer), status_code
