from . import auth
from .. import db, Bcrypt
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from .forms import SignupForm
from flask_login import login_user,current_user,login_required,logout_user








@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        # hashed_password = Bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account has been  created,you can log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template("auth/signup.html",title="Register", form = form) 

    return  render_template("auth/signup.html") 



    def __repr__(self):
        return f"User('{self.username}','{self.email}')"






@auth.route("/login")
def login():
    return  render_template("auth/login.html") 


@auth.route("/logout")
def logout():
    return render_template("auth/logout.html")






