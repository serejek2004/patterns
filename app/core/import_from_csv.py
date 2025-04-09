import os
import csv
from app.database import db
from app.models.models import Customer, ProjectManager, TechnicalSpecialist, Project, Task, Person, Employee
from decimal import Decimal
from datetime import datetime
from app.core.status_enum import StatusEnum


class CSVImporter:
    def __init__(self, directory):
        self.directory = directory

    @staticmethod
    def import_customers(file_path):
        with open(file_path, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                person = Person(
                    name=row["name"],
                    phone_number=row["phone_number"],
                    email=row["email"]
                )
                db.session.add(person)
                db.session.flush()

                customer = Customer(
                    id=person.id,
                    budget=Decimal(row["budget"]),
                    person=person
                )
                db.session.add(customer)

    @staticmethod
    def import_project_managers(file_path):
        with open(file_path, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                person = Person(
                    name=row["name"],
                    phone_number=row["phone_number"],
                    email=row["email"]
                )
                db.session.add(person)
                db.session.flush()

                employee = Employee(id=person.id, salary=Decimal(row["salary"]))
                db.session.add(employee)
                db.session.flush()

                pm = ProjectManager(id=employee.id)
                db.session.add(pm)

    @staticmethod
    def import_technical_specialists(file_path):
        with open(file_path, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                person = Person(
                    name=row["name"],
                    phone_number=row["phone_number"],
                    email=row["email"]
                )
                db.session.add(person)
                db.session.flush()

                employee = Employee(id=person.id, salary=Decimal(row["salary"]))
                db.session.add(employee)
                db.session.flush()

                ts = TechnicalSpecialist(id=employee.id, manager_id=int(row["manager_id"]))
                db.session.add(ts)

    @staticmethod
    def import_projects(file_path):
        with open(file_path, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                project = Project(
                    project_name=row["project_name"],
                    customer_id=int(row["customer_id"]),
                    project_manager_id=int(row["project_manager_id"]),
                    status=StatusEnum[row["status"]],
                    start_date=datetime.fromisoformat(row["start_date"]),
                    end_date=datetime.fromisoformat(row["end_date"]),
                    budget=Decimal(row["budget"])
                )
                db.session.add(project)

    @staticmethod
    def import_tasks(file_path):
        with open(file_path, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                task = Task(
                    status=StatusEnum[row["status"]],
                    deadline=datetime.fromisoformat(row["deadline"]),
                    doer_id=int(row["doer_id"]),
                    project_id=int(row["project_id"])
                )
                db.session.add(task)

    def import_all_files(self):
        for filename in os.listdir(self.directory):
            if filename == "customers.csv":
                self.import_customers(os.path.join(self.directory, filename))
            elif filename == "project_managers.csv":
                self.import_project_managers(os.path.join(self.directory, filename))
            elif filename == "technical_specialists.csv":
                self.import_technical_specialists(os.path.join(self.directory, filename))
            elif filename == "projects.csv":
                self.import_projects(os.path.join(self.directory, filename))
            elif filename == "tasks.csv":
                self.import_tasks(os.path.join(self.directory, filename))


def import_csv_from_directory():
    directory = "/Users/mac/Desktop/patterns/app/core/generated_csv"
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Error {directory} not found")

    CSVImporter(directory).import_all_files()

    db.session.commit()
