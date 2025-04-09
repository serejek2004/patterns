import csv
import os
import random
from datetime import datetime, timedelta
from faker import Faker


fake = Faker("uk_UA")

status_enum = ["NOT_STARTED", "IN_PROGRESS", "PAUSED", "DONE"]

customers = []
project_managers = []
technical_specialists = []
projects = []
tasks = []
for _ in range(20):
    for _ in range(10):
        customers.append({
            "name": fake.name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "budget": round(random.uniform(10000, 1000000), 2)
        })

    for _ in range(10):
        project_managers.append({
            "name": fake.name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "salary": round(random.uniform(1500, 5000), 2)
        })

    for i in range(10):
        technical_specialists.append({
            "name": fake.name(),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "salary": round(random.uniform(1000, 4000), 2),
            "manager_id": random.randint(200, 400)
        })

    for i in range(10):
        start = fake.date_between(start_date="-1y", end_date="today")
        end = start + timedelta(days=random.randint(30, 180))
        projects.append({
            "project_name": fake.bs().capitalize(),
            "customer_id": random.randint(1, 200),
            "project_manager_id": random.randint(200, 400),
            "status": random.choice(status_enum),
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            "budget": round(random.uniform(5000, 200000), 2)
        })

    for i in range(10):
        deadline = datetime.now() + timedelta(days=random.randint(1, 90))
        tasks.append({
            "status": random.choice(status_enum),
            "deadline": deadline.isoformat(),
            "doer_id": random.randint(400, 600),
            "project_id": random.randint(1, 200)
        })


def write_csv(filename, fieldnames, data):
    output_dir = os.path.join(os.path.dirname(__file__), "generated_csv")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


write_csv("customers.csv", ["name", "phone_number", "email", "budget"], customers)
write_csv("project_managers.csv", ["name", "phone_number", "email", "salary"], project_managers)
write_csv("technical_specialists.csv", ["name", "phone_number", "email", "salary", "manager_id"], technical_specialists)
write_csv("projects.csv", ["project_name", "customer_id", "project_manager_id", "status", "start_date", "end_date", "budget"], projects)
write_csv("tasks.csv", ["status", "deadline", "doer_id", "project_id"], tasks)
