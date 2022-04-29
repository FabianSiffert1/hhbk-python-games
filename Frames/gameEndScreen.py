from tkinter import *
from tkinter import ttk

class GameEndScreen:
    """Select Difficulty Content"""

    def __init__(self,vFrame, currentGame):

        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        winOrLoss = Label(frame, text= vFrame.winOrLossMessage)
        winOrLoss.grid(column=0, row=0, padx=5, pady=10)
        winOrLoss.config(bg="#CEBB8C", padx=0)

        gameButton = Button(frame, text="Neues Spiel", command= lambda: vFrame.openScreen("difficulty",game=currentGame))
        gameButton.grid(column=0, row=1, padx=5, pady=10)

        scoreboardButton = Button(frame, text="Scoreboard", command= lambda: vFrame.openScreen("scoreboard"))
        scoreboardButton.grid(column=0, row=2, padx=5, pady=10)

        exitButton = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start"))
        exitButton.grid(column=0, row=3, padx=5, pady=10)


        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()
        vFrame.mainWindow.frm.place(relx=0.5, rely=0.5, anchor=CENTER)

