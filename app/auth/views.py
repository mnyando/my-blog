from . import auth
from .. import db
from flask import render_template


@auth.route("/signup")
def signup():
    return  render_template("auth/signup.html")


@auth.route("/login")
def Login():
    return  render_template("Login.html") 


@auth.route("/logout")
def Logout():
    return render_template("Logout.html")

