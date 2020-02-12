from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from .nav import nav
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
nav.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.errors import bp as errors_bp

app.register_blueprint(errors_bp)

from app.main import bp as main_bp

app.register_blueprint(main_bp)

from app.api import bp as app_bp

app.register_blueprint(app_bp, url_prefix="/api")

# from app.auth import bp as auth_bp
# app.register_blueprint(auth_bp)
from app import models
from app import filters
