from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SubmitField, FileField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError
# from app.models import User, SearchQuery


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class QubeForm(FlaskForm):
    qube_wall_1 = FileField('icon1')
    qube_wall_2 = FileField('icon2')
    qube_wall_3 = FileField('icon3')
    qube_wall_4 = FileField('icon4')
    qube_wall_5 = FileField('icon5')
    qube_wall_6 = FileField('icon6')
    # qube_color =


'''
class SearchForm(FlaskForm):
    search_query = StringField('Plot id number:', validators=[DataRequired()])
    submit = SubmitField('Search')

    def validate_search_query(self, search_query):#verify plot number

'''