from app.database import db
from app.core.status_enum import StatusEnum


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    phone_number = db.Column(db.String(32))
    email = db.Column(db.String(100))

    employee = db.relationship('Employee', uselist=False, back_populates='person', cascade='all, delete-orphan')
    customer = db.relationship('Customer', uselist=False, back_populates='person', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email
        }


class Employee(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    salary = db.Column(db.Numeric(10, 2), nullable=False)

    person = db.relationship('Person', back_populates='employee')
    technical_specialist = db.relationship('TechnicalSpecialist',
                                           uselist=False,
                                           back_populates='employee',
                                           cascade='all, delete-orphan')
    project_manager = db.relationship('ProjectManager',
                                      uselist=False,
                                      back_populates='employee',
                                      cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'salary': str(self.salary),
            'person': self.person.to_dict() if self.person else None
        }


class Customer(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    budget = db.Column(db.Numeric)

    person = db.relationship('Person', back_populates='customer')
    project = db.relationship('Project', back_populates='customer', uselist=False)

    def to_dict(self):
        return {
            'budget': str(self.budget),
            'person': self.person.to_dict() if self.person else None,
            'project': self.project.to_dict() if self.project else None
        }


class ProjectManager(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)

    employee = db.relationship('Employee', back_populates='project_manager')
    project = db.relationship('Project', back_populates='manager')
    specialists = db.relationship('TechnicalSpecialist', back_populates='manager')

    def to_dict(self):
        return {
            'employee': self.employee.to_dict() if self.employee else None,
            'projects': [project.id for project in self.project] if self.project else [],
            'specialists': [specialist.id for specialist in self.specialists]
        }


class TechnicalSpecialist(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('project_manager.id'), nullable=False)

    manager = db.relationship('ProjectManager', back_populates='specialists')
    employee = db.relationship('Employee', back_populates='technical_specialist')
    task = db.relationship('Task', back_populates='doer', uselist=False)

    def to_dict(self):
        return {
            'manager': self.manager.id if self.manager else None,
            'employee': self.employee.to_dict() if self.employee else None,
            'tasks': self.task.id if self.task else None,
        }


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    project_manager_id = db.Column(db.Integer, db.ForeignKey('project_manager.id'))
    status = db.Column(db.Enum(StatusEnum))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    budget = db.Column(db.Numeric)

    customer = db.relationship('Customer', back_populates='project')
    manager = db.relationship('ProjectManager', back_populates='project')
    tasks = db.relationship('Task', back_populates='project')

    def to_dict(self):
        return {
            'id': self.id,
            'project_name': self.project_name,
            'customer': self.customer.id if self.customer else None,
            'manager': self.manager.id if self.manager else None,
            'status': self.status.name if self.status else None,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'budget': str(self.budget)
        }


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(StatusEnum))
    deadline = db.Column(db.DateTime)

    doer_id = db.Column(db.Integer, db.ForeignKey('technical_specialist.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    project = db.relationship('Project', back_populates='tasks')
    doer = db.relationship('TechnicalSpecialist', back_populates='task')

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status.name if self.status else None,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'doer': self.doer.id if self.doer else None,
            'project': self.project.id if self.project else None
        }
