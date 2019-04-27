import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static', instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')
# Now we can access the configuration variables via app.config["VAR_NAME"].
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
from app import views, models
db.create_all()