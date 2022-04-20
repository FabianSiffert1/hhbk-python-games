from tkinter import *
from tkinter import ttk

class SelectDifficulty:
    """Select Difficulty Content"""

    global vFrame 

    def __init__(self,vFrame):

        frame = ttk.Frame(vFrame.mainWindow, padding=10)

        d = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start"))
        d.pack(pady=20)

        a = Button(frame, text="Easy", command= lambda: vFrame.openScreen("game"))
        a.pack(pady=20)

        b = Button(frame, text="Medium", command= lambda: vFrame.openScreen("game"))
        b.pack(pady=20)

        c = Button(frame, text="Hard", command= lambda: vFrame.openScreen("game"))
        c.pack(pady=20)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()

