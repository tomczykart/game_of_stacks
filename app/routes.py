from flask import render_template, flash, redirect, url_for, session, request
from app import app, db
from app.forms import SearchForm
from app.models import User, SearchQuery
from app.get_data import get_coordinates, generate_map, plot_area, parse_xml

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    #flash(current_user)
    #logic for search form submit
    form = SearchForm()
    if form.validate_on_submit():
        session['query'] = request.form.get('search_query')

        #get data from external api
        return redirect(url_for('/))
    #render index page
    return render_template('index.html', title = 'HOME', form = form)
