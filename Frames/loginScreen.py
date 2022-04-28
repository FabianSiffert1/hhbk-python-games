from dataclasses import dataclass
from tkinter import *
import sqlite3

from Datenbaken.database import Database

db = sqlite3.connect("Scoreboard.db")
c = db.cursor()

class loginScreen:
    """"loginScreen Content"""

    global usernameEntryBox
    global passwordEntryBox
    global registerButton
    global loginButton
    global error
    global vFrame

    def __init__(self, vFrame):
        self.vFrame = vFrame
        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        database = Database()

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

        

        self.loginButton = Button(frame, text="Login", command=lambda: database.loginUser(self,self.usernameEntryBox.get(), self.passwordEntryBox.get()))
        self.loginButton.grid(column=2, row=6, padx=5, pady=2.5)


        self.registerButton = Button(frame, text="Register", command= lambda: database.addNewUser(self,self.usernameEntryBox.get(), self.passwordEntryBox.get()))
        self.registerButton.grid(column=3, row=6, padx=5, pady=2.5)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()
        vFrame.database = database
