from flask_wtf  import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
#from app.models import User, SearchQuery


'''
class SearchForm(FlaskForm):
    search_query = StringField('Plot id number:', validators=[DataRequired()])
    submit = SubmitField('Search')

    def validate_search_query(self, search_query):#verify plot number

'''