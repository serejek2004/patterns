from flask import Flask
from app.config import Config
from app.database import db
from app.project.views import view_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(view_bp)
db.init_app(app)

from app.customer import controller
from app.project_manager import controller
from app.technical_specialist import controller
from app.project import controller
from app.task import controller
