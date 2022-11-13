from flask import render_template, flash, redirect, url_for, session, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User, UserCube
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # render index page
    return render_template('index.html', title='HOME')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user is already login redirect him to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # login form submitted
    form = LoginForm()
    if form.validate_on_submit():
        # assign user data with database query
        user = User.query.filter_by(username=form.username.data).first()
        # check for user and his password
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # login user
        login_user(user, remember=form.remember_me.data)
        flash('Successfully logged in')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # if user is already login redirect him to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # set up registration
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, confirmed=False)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New user added')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/add_cube', methods=['GET', 'POST'])
@login_required
def add_cube():
    return render_template('add_cube.html', title='Add Cube')
