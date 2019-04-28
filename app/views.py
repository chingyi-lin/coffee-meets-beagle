from flask import render_template, redirect, request, url_for, flash, json, Response
from app import app, models, login_manager, db, user, animal, donation, intention
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, SignUpForm
from .user import User
from .animal import Animal
from .donation import Donation
from .intention import Intention
from .models import *

# --- Endpoints: --- #
@app.route('/user/signup', methods=['POST'])
def signup():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        age = request.form.get('age')
        if isUsernameUsed(username) is True:
            # in this case user with this username exists already
            data = { "Error": "Username is already used. Please pick a different one." }
            status_code = 409
        if isEmailUsed(email) is True:
            # in this case user with this username exists already
            data = { "Error": "Email is already used. Please pick a different one." }
            status_code = 409
        newUser = User(username, email, age)
        newUser.set_password(password)
        addToDatabase(newUser)
        login_user(newUser)
        data = { "user_id": newUser.id}
        status_code = 201
    else:
        data = { "answer": "Bad request header" }
        status_code = 400
    resp = Response(json.dumps(data), status=status_code, mimetype='application/json')
    return resp

@app.route('/user/login', methods=['POST'])
def login():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        username = request.form.get('username')
        password = request.form.get('password')
        if validateLogin(username, password):
            data = { "user_id": current_user.id}
            status_code = 200
        else:
            data = { "error": "The login information is not corrected" }
            status_code = 403
    resp = Response(json.dumps(data), status=status_code, mimetype='application/json')
    return resp

# --- Page rendering methods: --- #
# It's just for UI. We can remove it later.

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', username = current_user.username)
    else:
        return render_template('index.html', username = "Guest")

@app.route('/signup', methods=['GET', 'POST'])
def signupPage():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        age = form.age.data
        if isUsernameUsed(username) is True:
            # in this case user with this username exists already
            flash("Username is already used. Please pick a different one.")
            return render_template('signup.html', title = "Sign Up", form = form)
        if isEmailUsed(email) is True:
            # in this case user with this username exists already
            flash("Email is already used. Please pick a different one.")
            return render_template('signup.html', title = "Sign Up", form = form)
        # in case it does not exist
        newUser = User(username, email, age)
        newUser.set_password(password)
        addToDatabase(newUser)
        login_user(newUser)
        return redirect(url_for('index'))
    return render_template('signup.html', title = "Sign Up", form = form, username = "Guest")


@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if validateLogin(username, password):
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', title = 'Log In', form = form, username = "Guest")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))