from . import auth
from .. import db
from flask import render_template


@auth.route("/signup")
def signup():
    return  render_template("auth/signup.html")


@auth.route("/login")
def login():
    return  render_template("auth/login.html") 


@auth.route("/logout")
def logout():
    return render_template("auth/logout.html")

