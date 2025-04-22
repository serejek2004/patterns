from flask import Blueprint, render_template, request, redirect, url_for
from app.project.dto import ProjectDTO
from app.project.service import ProjectService
from app.core.status_enum import StatusEnum
from app import db

view_bp = Blueprint('project_views', __name__)
project_service = ProjectService(db=db)


@view_bp.route('/project')
def show_projects():
    projects, _ = project_service.get_all()
    return render_template('project/list.html', projects=projects)


@view_bp.route('/project/<int:id>')
def show_project(id):
    project, _ = project_service.get_project_by_id(id)
    return render_template('project/detail.html', project=project)


@view_bp.route('/project/new', methods=['GET', 'POST'])
def create_project_view():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        project_dto = ProjectDTO.from_request(data=form_data)
        project_service.create_project(project_dto)
        return redirect(url_for('project_views.show_projects'))
    return render_template('project/form.html', project=None, statuses=StatusEnum.__members__.keys())


@view_bp.route('/project/<int:id>/edit', methods=['GET', 'POST'])
def edit_project_view(id):
    project, _ = project_service.get_project_by_id(id)
    if request.method == 'POST':
        form_data = request.form.to_dict()
        project_dto = ProjectDTO.from_request(data=form_data)
        project_service.update_project_by_id(id=id, project_dto=project_dto)
        return redirect(url_for('project_views.show_project', id=id))
    return render_template('project/form.html', project=project, statuses=StatusEnum.__members__.keys())


@view_bp.route('/project/<int:id>/delete', methods=['POST'])
def delete_project_view(id):
    project_service.delete_project_by_id(id)
    return redirect(url_for('project_views.show_projects'))
