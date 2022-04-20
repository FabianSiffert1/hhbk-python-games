from tkinter import *
from tkinter import ttk

class StartScreen:
    """Start Screen Content"""

    global vFrame
    def __init__(self,vFrame):
        frame = ttk.Frame(vFrame.mainWindow, padding=10)

        a = Button(frame, text="StartGame", command= lambda: vFrame.openScreen("difficulty"))
        a.pack(pady=20)

        b = Button(frame, text="Scoreboard", command= lambda: vFrame.openScreen("scoreboard"))
        b.pack(pady=20)


        b = Button(frame, text="Settings", command= lambda: vFrame.openScreen("settings"))
        b.pack(pady=20)

        c = Button(frame, text="Quit", command= vFrame.mainWindow.destroy)
        c.pack(pady=20)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()