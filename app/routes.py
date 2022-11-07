from flask import render_template, flash, redirect, url_for, session, request
from app import app, db
#from app.forms import SearchForm
#from app.models import User, SearchQuery


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    #render index page
    return render_template('index.html', title = 'HOME')
