from tkinter import *
import sqlite3

db = sqlite3.connect("Scoreboard.db")
c = db.cursor()
class Database:

    def addNewUser(self,loginScreen, newUsername, newPassword):
        print(newUsername, newPassword)
        # result = c.execute("SELECT COUNT(*) from users WHERE username =' + newusername + '")
        c.execute("SELECT COUNT(*) FROM users WHERE username = ?", (newUsername,))
        result = c.fetchone()
        #print(int(result[0]))

        if int(result[0]) > 0:
            loginScreen.error["text"] = "ERROR: Username already exists"
        else:
            loginScreen.error["text"] = "Added New User"
            c.execute("INSERT INTO users (username,password)"
                      " VALUES(?,?)", (newUsername, newPassword))
            db.commit()


    def loginUser(self,loginScreen, newUsername, newPassword):
        print(newUsername, newPassword)
        # result = c.execute("SELECT COUNT(*) from users WHERE username =' + newusername + '")
        c.execute("SELECT username, password  FROM users WHERE username = ?", (newUsername,))
        result = c.fetchone()
        #print(result[1])
        #print(result[0])
        if type(result) == "NoneType":
            loginScreen.error["text"] = "ERROR: Entry denied"
        elif result[0] == newUsername and str(result[1]) == str(newPassword):
            loginScreen.error["text"] = "Entry granted"
            loginScreen.vFrame.username = newUsername
            # Hier mus dann die Weiterleitung auf die Seite hin      <---
        else:
            loginScreen.error["text"] = "ERROR: Entry denied"

    def insertScoreboard(self,score,username):
        """Insert Score to Scoreboard"""
