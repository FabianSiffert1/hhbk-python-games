from tkinter import *
from tkinter import ttk

class SelectDifficulty:
    """Select Difficulty Content"""

    def __init__(self,vFrame):

        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        d = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start"))
        d.pack(pady=20)

        a = Button(frame, text="Easy", command= lambda: vFrame.openScreen("game"))
        a.pack(pady=20)

        b = Button(frame, text="Medium", command= lambda: vFrame.openScreen("game"))
        b.pack(pady=20)

        c = Button(frame, text="Hard", command= lambda: vFrame.openScreen("game"))
        c.pack(pady=20)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.place(relx=0.5, rely=0.5, anchor=CENTER)

