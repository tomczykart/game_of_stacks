from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_cube = db.relationship('UserCube', backref='cube_owner', lazy='dynamic')
    # define text representation when instance is called

    def __repr__(self):
        return f'<User id: {self.id}, and email: {self.email}>'

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
    time_created = db.Column(db.DateTime(timezone=True), index=True, server_default=db.func.utcnow())
    
    def __repr__(self):
        return f'<New cube created: {self.qube_id}, owner: {self.owner}>'
