from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SubmitField, FileField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from app.models import User, UserCube


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already taken')


class CubeForm(FlaskForm):
    cube_wall_1 = FileField('icon1')
    cube_wall_2 = FileField('icon2')
    cube_wall_3 = FileField('icon3')
    cube_wall_4 = FileField('icon4')
    cube_wall_5 = FileField('icon5')
    cube_wall_6 = FileField('icon6')
    submit = SubmitField('Add Cube')
    # cube_color =
    