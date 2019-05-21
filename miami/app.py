import os
import sqlite3
import calendar

from flask import Flask, render_template, request, session, url_for, redirect, flash
from datetime import datetime
from passlib.hash import md5_crypt

from util import dbCommands as db


app = Flask(__name__)

app.secret_key = "\x16\xc6w\x1c.!-\xb5\x15\x82u\xbe\x01\xc5?[\x18\n~\x891_\xa3\x9a}\xe6\x13\xea~\xc1\x92\xb8"

#the following is for the ajax timer
curr_hr = datetime.now().hour
curr_min = datetime.now().minute
curr_sec = datetime.now().second

def is_logged_in():
    return "id" in session

@app.route("/")
def home():
    if( is_logged_in() ):
        return render_template("home.html")
    else:
        return render_template("login.html")


@app.route("/auth" , methods = ["POST"])
def authenticate():
    '''Checks if the username and password entered match what's on file'''
    user_data = db.get_all_user_data()
    username = request.form.get("username")
    password = request.form.get("password")
    session["username"] = username
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
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    curr_table = calendar.monthcalendar(curr_year, curr_month)
    month_name = calendar.month_abbr[curr_month]
    return render_template("calendar.html", month = month_name, year = curr_year, table = curr_table)

@app.route("/templates", methods=["POST", "GET"])
def templates():
    userId=session["id"]
    names = db.get_all_templates(userId)
    print(userId)
    print(names)
    if request.method == 'POST':
        name = request.form["username"]
        task = request.form.getlist("task")
        start = request.form.getlist("start")
        end = request.form.getlist("end")
        counter = 0
        lists = []
        while counter < len(task):
            lists.append([userId, name, task[counter], start[counter], end[counter]])
            counter += 1
        db.add_All_to_template(lists)
        names = db.get_all_templates(userId)
        return render_template("template.html",templates = names)
    else:
        return render_template("template.html",templates=names)

@app.route("/create",methods=["POST","GET"])
def create():
    return render_template("create.html")

if __name__ == "__main__":
    app.debug = True
    app.run()