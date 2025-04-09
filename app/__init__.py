from flask import Flask
from app.config import Config
from app.database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from app.customer import controller
from app.project_manager import controller
from app.technical_specialist import controller
from app.project import controller
from app.task import controller
