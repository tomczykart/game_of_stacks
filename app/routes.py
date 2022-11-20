from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.token import generate_token, confirm_token
from app.forms import LoginForm, RegisterForm
from app.models import User  # UserCube
from app.email import send_email
from app.decorators import check_confirmed
from werkzeug.urls import url_parse
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # render index page
    flash('Test message, nooydysdfsf2 2 sawsome')
    flash('2Test message, nooydysdfsf2 2 sawsome')
    flash('3statataTest message, nooydysdfsf2 2 sawsome')
    flash('4Test')
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
        # add user to database
        user = User(username=form.username.data, email=form.email.data, confirmed=False)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New user added')
        # confirm email section
        token = generate_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('confirmation_email.html', confirm_url=confirm_url)
        subject = "Game of Stacks email confirmation"
        send_email(user.email, subject, html)
        flash('Confirmation email sent')
        # login the user
        login_user(user)
        # redirect to unconfirmed
        return redirect(url_for('unconfirmed'))
    return render_template('register.html', title='Register', form=form)


@app.route('/confirm/<token>')
@login_required
def confirm_email(token):
    email = ''
    try:
        email = confirm_token(token)
    except Exception as e:
        flash(f'Confirmation link is invalid or it has expired \n Error:{e}')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('User already confirmed.')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Email confirmed')
    return redirect(url_for('index'))


@app.route('/resend')
@login_required
def resend():
    token = generate_token(current_user.email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('confirmation_email.html', confirm_url=confirm_url)
    subject = "Game of Stacks email confirmation"
    send_email(current_user.email, subject, html)
    flash('Confirmation email sent')
    return redirect(url_for('unconfirmed'))


@app.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        redirect(url_for('index'))
    flash('confirm your email')
    return render_template('unconfirmed.html', title='Unconfirmed')


@app.route('/addcube', methods=['GET', 'POST'])
@login_required
@check_confirmed
def addcube():
    return render_template('addcube.html', title='Add Cube')
