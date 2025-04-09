from flask_sqlalchemy import SQLAlchemy
from app.core.dao import BasicDAO


class ProjectDAO(BasicDAO):
    def __init__(self, db: SQLAlchemy):
        self.db = db
