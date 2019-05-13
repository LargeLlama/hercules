import os
import sqlite3

from flask import Flask, render_template, request, session, url_for, redirect, flash
from passlib.hash import md5_crypt

from util import dbCommands as db

app = Flask(__name__)

app.secret_key = os.urandom(32)

user_data = db.get_all_user_data()

def is_logged_in():
    return "id" in session

@app.route("/")
def home():
    if(is_logged_in()):
        return render_template("home.html")
    else:
        return render_template("login.html")


@app.route("/auth" , methods = ["POST"])
def authenticate():
    user_data = db.get_all_user_data()
    username = request.form.get("username")
    password = request.form.get("password")
    if username in user_data:
        if md5_crypt.verify(password, user_data[username]):
            id = db.get_user_id(username)
            session["id"] = id
        else:
            flash("Invalid password, try again!")
    else:
        flash("Invalid username, try again!")
    return redirect(url_for('home'))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registerAuth", methods = ["POST"])
def reg_auth():
    user_data = db.get_all_user_data()
    username = request.form.get("username")
    password = request.form.get("password")
    password2 = request.form.get("password2")
    if username in user_data:
        flash("Username already exists! Please pick another one!")
        return redirect(url_for("register"))
    elif len(username) < 4:
        flash("Username has to be at least 4 characters!")
        return redirect(url_for("register"))
    elif password != password2:
        flash("Input Same Password in Both Fields!")
        return redirect(url_for("register"))
    else:
        db.add_user(username, md5_crypt.encrypt(password))
        flash("Successfully Registered, Now Sign In!")
        return redirect(url_for('home'))


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("id")
    return redirect(url_for("home"))

@app.route("/calendar")
def cal():
    return render_template("calendar.html")

@app.route("/lol", methods=["GET"])
def lol():
    return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
