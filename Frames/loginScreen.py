from tkinter import *
import sqlite3

db = sqlite3.connect("Scoreboard.db")
c = db.cursor()

class loginScreen:
    """"loginScreen Content"""

    global usernameEntryBox
    global passwordEntryBox
    global registerButton
    global loginButton
    global error

    def __init__(self, vFrame):
        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        self.error = Message(frame, text="", width=180)
        self.error.grid(column=0, row=8)

        self.usernameEntryBox = Entry()
        self.usernameEntryBox = Entry(frame, width=20)
        #self.usernameEntryBox.insert(END, 'Username')
        self.usernameEntryBox.grid(column=2, row=2,  columnspan=30)

        userNameEntryBoxLabel = Label(frame, text="Enter Username")
        userNameEntryBoxLabel.grid(column=0, row=2)

        self.passwordEntryBox = Entry()
        self.passwordEntryBox = Entry(frame, width=20)
        #passwordEntryBox.insert(END, 'Password')
        self.passwordEntryBox.grid(column=2, row=3,  columnspan=30)

        passwordNameEntryBoxLabel = Label(frame, text="Enter Password")
        passwordNameEntryBoxLabel.grid(column=0, row=3)

        Button(frame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)


        self.loginButton = Button(frame, text="Login", command=lambda: self.loginUser(self.usernameEntryBox.get(), self.passwordEntryBox.get()))
        self.loginButton.grid(column=2, row=6, padx=5, pady=2.5)


        self.registerButton = Button(frame, text="Register", command= lambda: self.addNewUser(self.usernameEntryBox.get(), self.passwordEntryBox.get()))
        self.registerButton.grid(column=3, row=6, padx=5, pady=2.5)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()

    def addNewUser(self, newUsername, newPassword):
        print(newUsername, newPassword)
        # result = c.execute("SELECT COUNT(*) from users WHERE username =' + newusername + '")
        c.execute("SELECT COUNT(*) FROM users WHERE username = ?", (newUsername,))
        result = c.fetchone()
        #print(int(result[0]))

        if int(result[0]) > 0:
            self.error["text"] = "ERROR: Username already exists"
        else:
            self.error["text"] = "Added New User"
            c.execute("INSERT INTO users (username,password)"
                      " VALUES(?,?)", (newUsername, newPassword))
            db.commit()


    def loginUser(self, newUsername, newPassword):
        print(newUsername, newPassword)
        # result = c.execute("SELECT COUNT(*) from users WHERE username =' + newusername + '")
        c.execute("SELECT username, password  FROM users WHERE username = ?", (newUsername,))
        result = c.fetchone()
        print(result[1])
        print(result[0])

        if result[0] == newUsername and str(result[1]) == str(newPassword):
            self.error["text"] = "Entry granted"
            # Hier mus dann die Weiterleitung auf die Seite hin      <---
        else:
            self.error["text"] = "ERROR: Entry denied"
