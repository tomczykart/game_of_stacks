from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_login import LoginManager

# create flask instance and load its configuration
app = Flask(__name__)
app.config.from_object(Config)

# create database instance
db = SQLAlchemy(app)
#create database migration engine obcjct
migrate = Migrate(app, db)

# initialize LoginMenager extension
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
