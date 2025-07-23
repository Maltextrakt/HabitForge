#The different routes for the application

#imports
from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import User
from app.auth.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            flash("Login succesful!", "success")
            return redirect(url_for("dashboard.user_dashboard"))
        else:
            flash("Invalid email or password", "danger")
    else:
        print(form.errors)

    print("Error, could not log in")
    return render_template("auth/login.html", form=form)

@auth.route("/register", methods=["GET", "POST"])
def register():
    from app import db
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully! You can now log in.", "Success")
        return redirect(url_for("auth.login"))
    
    return render_template("auth/register.html", form=form)
