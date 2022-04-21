from tkinter import *
from tkinter import ttk

class ScoreBoardScreen:
    """Scoreboard Screen Content"""

    def __init__(self,vFrame):
        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        a = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start"))
        a.pack(pady=20)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()