from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from .nav import nav

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
nav.init_app(app)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.main import bp as main_bp
app.register_blueprint(main_bp)

#from app import routes
