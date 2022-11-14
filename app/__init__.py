from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

# create flask instance and load its configuration
app = Flask(__name__)
app.config.from_object(Config)

# create database instance
db = SQLAlchemy(app)
# create database migration engine object
migrate = Migrate(app, db)

# initialize LoginManager extension
login = LoginManager(app)
login.login_view = 'login'

# initialize mail extension
mail = Mail(app)

from app import routes, models
