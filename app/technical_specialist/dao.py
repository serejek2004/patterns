from flask_sqlalchemy import SQLAlchemy
from app.core.dao import BasicDAO


class TechnicalSpecialistDAO(BasicDAO):
    def __init__(self, db: SQLAlchemy):
        self.db = db
