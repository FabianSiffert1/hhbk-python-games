from tkinter import *
import sqlite3

db = sqlite3.connect("Scoreboard.db")
c = db.cursor()



c.execute(""" CREATE TABLE IF NOT EXISTS scoreboard (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT    NOT NULL,
    score    INTEGER,
    game    INTEGER 
 ); 
 
""")


c.execute("""CREATE TABLE If Not Exists users (
    id       INTEGER PRIMARY KEY NOT NULL ,
    username TEXT NOT NULL,
    password INTEGER NOT NULL
);

""")





def add_new_user():
    newusername = username.get()
    newpassword = password.get()
    print(newusername)

    #result = c.execute("SELECT COUNT(*) from users WHERE username =' + newusername + '")
    c.execute("SELECT COUNT(*) FROM users WHERE username = ?", (newusername,))
    result = c.fetchone()
    print(int(result[0]))

    if int(result[0]) > 0:
        error["text"] = "ERROR: Username already exists"
    else:
        error["text"] = "Added New User"
        c.execute("INSERT INTO users (username,password)"
                  " VALUES(?,?)",(newusername,newpassword))
        db.commit()


def login_user():
    newusername = username.get()
    newpassword = password.get()
    #print(newusername)

    #result = c.execute("SELECT COUNT(*) from users WHERE username =' + newusername + '")
    c.execute("SELECT username, password  FROM users WHERE username = ?", (newusername,))
    result = c.fetchone()
    print(result[1])

    if result[0] == newusername and str(result[1]) == str(newpassword):
        error["text"] = "Entry granted"
        #Hier mus dann die Weiterleitung auf die Seite hin      <---
    else:
        error["text"] = "ERROR: Entry denied"



window = Tk()
window.title("Secureserv")
window.geometry("450x180")

error = Message(text= "", width = 180)
error.place(x = 30, y = 10)
error.config(padx = 0 )

label1 = Label(text = " Enter Username ")
label1.place(x = 30, y = 40)
label1.config(bg = 'lightblue', padx = 0)

label2 = Label(text = " Enter Password  ")
label2.place(x = 30, y = 90)
label2.config(bg = 'lightblue', padx = 0)

username = Entry(text = "")
username.place (x = 150, y = 40, width = 200, height = 25)

password = Entry(text = "")
password.place (x = 150, y = 90, width = 200, height = 25)


Register = Button(text = 'Register', command = add_new_user)
Register.place(x = 160, y = 130, width = 75, height= 35)

Login = Button(text = 'Login', command = login_user)
Login.place(x = 260, y = 130, width = 75, height= 35)

scoreboard = Button(text = 'scoreboard', command = scoreboardContent)
scoreboard.place(x = 360, y = 130, width = 75, height= 35)

#Commit changes
db.commit()
#Close Connection
#db.close()

window.mainloop()



