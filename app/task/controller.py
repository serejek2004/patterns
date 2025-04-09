from app import app, db
from flask import request, jsonify
from app.task.dto import TaskDTO
from app.task.service import TaskService
from app.core.status_enum import StatusEnum

TaskService = TaskService(db)


@app.route('/task', methods=['POST'])
def register_task():
    data = request.get_json()

    if data['status'] not in StatusEnum.__members__:
        return jsonify({"message": "Bad request"}), 400

    task_dto = TaskDTO.from_request(data=data)
    response, status_code = TaskService.register_task(task_dto=task_dto)

    if status_code != 201:
        return jsonify({"message": f"{response}"}), status_code

    return jsonify(response), 201


@app.route('/task', methods=['GET'])
def get_all_tasks():
    response, status_code = TaskService.get_all()

    return jsonify(response), status_code


@app.route('/task/<int:id>', methods=['GET'])
def get_task_by_id(id: int):
    response, status_code = TaskService.get_task_by_id(id=id)

    return jsonify(response), status_code


@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task_by_id(id: int):
    response, status_code = TaskService.delete_task_by_id(id=id)

    return jsonify({"message": response}), status_code


@app.route('/task/<int:id>', methods=['PUT'])
def update_task_by_id(id: int):
    data = request.get_json()

    if data['status'] not in StatusEnum.__members__:
        return jsonify({"message": "Bad request"}), 400

    task_dto = TaskDTO.from_request(data)
    response, status_code = TaskService.update_task_by_id(task_dto=task_dto, id=id)

    if status_code != 200:
        return {"Message": f"{response}"}, status_code

    return jsonify(response), status_code
