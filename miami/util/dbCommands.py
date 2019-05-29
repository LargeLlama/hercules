#util commands for messing with the database
import sqlite3
DB_FILE ="data/data.db"
#----------------when you want to add data to the database------------------------------
#adds to the users table
def add_user(username,password_hash):
    '''adds users to use table'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO users (username,password_hash)VALUES(?,?);"
    c.execute(command,(username,password_hash))
    db.commit()
    db.close()
#adds to the calender table
def add_Calender(user_id,date,schedule_name):
    '''adds a calender entry for a user'''
    db = sqlite3.connect(DB_FILE)
    c= db.cursor()
    command = "INSERT INTO calender(user_id,date,schedule_name)VALUES(?,?,?);"
    c.execute(command,(user_id,date,schedule_name))
    db.commit()
    db.close()

def add_template(user_id,name,task,start_time,end_time):
    '''adds a template that a user has made into the table'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO templates(user_id,name,task,start_time,end_time)VALUES(?,?,?,?,?);"
    c.execute(command,(user_id,name,task,start_time,end_time))
    db.commit()
    db.close()

#given a list of tuples itll add all of em to the table
def add_All_to_template(list):
    '''adds every line of a template to the templates table given a list of tuples'''
    for each in list:
        add_template(each[0],each[1],each[2],each[3],each[4])

#--------------------useful for logins---------------------------
#returns username password combo in a dict in the format username:password
def get_all_user_data():
    '''gets all user data into a dict'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command  = "SELECT username,password_hash FROM users;"
    c.execute(command)
    userInfo = c.fetchall()
    db.close()
    dict = {}
    for item in userInfo:
        dict[item[0]] = item[1]
    return dict

#returns user id based on username every username is unique so this shouldn't be an issue
def get_user_id(username):
    '''gets user id based on username'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id FROM users WHERE username = ?;"
    c.execute(command,(username,))
    user_id = c.fetchall()
    db.close()
    return user_id[0][0]

#retrieve username based on id
def get_username(id):
    '''get username based on id'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username FROM users WHERE id = ?;"
    c.execute(command,(id,))
    name = c.fetchall()
    db.close()
    return name[0][0]



#-----------for calender table-------
def get_template(user_id,name):
    '''gets a template from the template table based on id of user and name of template'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT task,start_time,end_time FROM templates WHERE user_id = ? AND name = ?;"
    c.execute(command,(user_id,name))
    template = c.fetchall()
    db.close()
    #should return as a list of tuples
    return template



def get_all_templates(user_id):
    #gets all individual template namses from the templates table based on id of user
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT name FROM templates WHERE user_id = ?;"
    c.execute(command,(user_id,))
    templates = c.fetchall()
    return templates



def get_template_from_date(user_id,date):
    '''gets a template from the calender based on date given'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    print(date)
    command = "SELECT schedule_name FROM calender WHERE user_id = ? AND date LIKE ?;"
    date = "%" + date + "%"
    c.execute(command,(user_id, date))
    name = c.fetchall()
    print("NAME", name)
    if name:
        name = name[0][0]
    return name

