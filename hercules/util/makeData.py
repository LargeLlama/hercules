import sqlite3

db = sqlite3.connect("/var/www/hercules/hercules/data/data.db")
c = db.cursor()
#create users
command = "CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password_hash TEXT)"
c.execute(command)
#create calendar
command = "CREATE TABLE calender(user_id INTEGER, date TEXT,schedule_name TEXT)"
c.execute(command)
#create templates
command = "CREATE TABLE templates(user_id INTEGER,name TEXT,task TEXT,start_time TEXT,end_time TEXT)"
c.execute(command)
db.commit()
db.close()
