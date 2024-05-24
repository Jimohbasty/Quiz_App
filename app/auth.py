from flask import Blueprint, render_template, url_for, flash
from flask_login import login_user
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app import db
bp = Blueprint("auth",__name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/login", methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return "God is really good"
        else:
            return "God is most wonderful"
    return render_template("login.html", form = form)


@bp.route("/register", methods = ["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # check for register email
        exiting_email = User.query.filter_by(email = form.email.data).first()

        if exiting_email:
            flash('Email is already registered. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
        # checking if the username exit
        existing_username = User.query.filter_by(username=form.username.data).first()
        if existing_username:
            flash('Username is already taken. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
        user = User( username = form.username.data, 
                    email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return("Userinfo save successfully")
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template("register.html", form = form)

