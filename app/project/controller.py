from app import app, db
from flask import request, jsonify
from app.project.dto import ProjectDTO
from app.project.service import ProjectService
from app.core.status_enum import StatusEnum

ProjectService = ProjectService(db)


@app.route('/project', methods=['POST'])
def create_project():
    data = request.get_json()

    if data['status'] not in StatusEnum.__members__:
        return jsonify({"message": "Bad request"}), 400

    project_dto = ProjectDTO.from_request(data=data)
    response, status_code = ProjectService.create_project(project_dto=project_dto)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    return jsonify(response), 201


@app.route('/project', methods=['GET'])
def get_all_projects():
    response, status_code = ProjectService.get_all()

    return jsonify(response), status_code


@app.route('/project/<int:id>', methods=['GET'])
def get_project_by_id(id: int):
    response, status_code = ProjectService.get_project_by_id(id=id)

    return jsonify(response), status_code


@app.route('/project/<int:id>', methods=['DELETE'])
def delete_project_by_id(id: int):
    response, status_code = ProjectService.delete_project_by_id(id=id)

    return jsonify({"message": response}), status_code


@app.route('/project/<int:id>', methods=['PUT'])
def update_project_by_id(id: int):
    data = request.get_json()

    if data['status'] not in StatusEnum.__members__:
        return jsonify({"message": "Bad request"}), 400

    project_dto = ProjectDTO.from_request(data)
    response, status_code = ProjectService.update_project_by_id(project_dto=project_dto, id=id)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    return jsonify(response), status_code
