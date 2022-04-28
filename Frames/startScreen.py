from tkinter import *
from tkinter import ttk

class StartScreen:
    """Start Screen Content"""

    def __init__(self,vFrame):
        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        buttonFrame = Frame(frame, bg="#CEBB8C")

        loginButton = Button(frame, text="Login", command= lambda: vFrame.scoreboardContent())
        loginButton.grid(column=0,row=4,padx=5,pady=2.5)

        bauerButton = Button(buttonFrame, text="Bauer", command= lambda: vFrame.openScreen("difficulty",game="schach"))
        bauerButton.grid(column=0,row=0,padx=5)

        damenButton = Button(buttonFrame, text="Dame", command= lambda: vFrame.openScreen("difficulty",game="dame"))
        damenButton.grid(column=1,row=0,padx=5)

        buttonFrame.grid(column=0,row=0,padx=5,pady=2.5)

        scoreboardButton = Button(frame, text="Scoreboard", command= lambda: vFrame.openScreen("scoreboard"))
        scoreboardButton.grid(column=0,row=1,padx=5,pady=2.5)


        settingsButton = Button(frame, text="Settings", command= lambda: vFrame.openScreen("settings"))
        settingsButton.grid(column=0,row=2,padx=5,pady=2.5)

        quitButton = Button(frame, text="Quit", command= vFrame.mainWindow.destroy)
        quitButton.grid(column=0,row=3,padx=5,pady=2.5)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.place(relx=0.5, rely=0.5, anchor=CENTER)