from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    user_cube = db.relationship('UserCube', backref='cube_owner', lazy='dynamic')

    def __init__(self, username, email, confirmed, confirmed_on=None, admin=False):
        self.username = username
        self.email = email
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
        self.admin = admin
        self.registered_on = datetime.now()

    def __repr__(self):  # define text representation when instance is called
        return f'<User id: {self.id}, username:{self.username} and email: {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserCube(UserMixin, db.Model):
    cube_id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    cube_position = db.Column(db.Integer(), index=True)
    cube_floor = db.Column(db.Integer, index=True)
    cube_color = db.Column(db.String(8), index=True)
    cube_wall1 = db.Column(db.String(1600), index=True)
    cube_wall2 = db.Column(db.String(1600), index=True)
    cube_wall3 = db.Column(db.String(1600), index=True)
    cube_wall4 = db.Column(db.String(1600), index=True)
    cube_wall5 = db.Column(db.String(1600), index=True)
    cube_wall6 = db.Column(db.String(1600), index=True)
    time_created = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f'<New cube created: {self.qube_id}, owner: {self.owner}>'
