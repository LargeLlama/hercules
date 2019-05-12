import sqlite3

db = sqlite3.connect("data/data.db")
c = db.cursor()
#create users
command = "CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password_hash TEXT)"
c.execute(command)
#create contributions
command = "CREATE TABLE calender(user_id INTEGER, date TEXT,schedule_name TEXT)"
c.execute(command)
#create stories
command = "CREATE TABLE templates(user_id INTEGER,name TEXT,task TEXT,start_time INTEGER,end_time INTEGER)"
c.execute(command)
db.commit()
db.close()
