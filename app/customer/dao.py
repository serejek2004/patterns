from flask_sqlalchemy import SQLAlchemy
from app.core.dao import BasicDAO


class CustomerDAO(BasicDAO):
    def __init__(self, db: SQLAlchemy):
        self.db = db
