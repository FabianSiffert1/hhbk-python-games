from tkinter import *
from tkinter import ttk

class SettingsScreen:
    """Settings Screen Content"""

    global vFrame
    def __init__(self,vFrame):
        frame = ttk.Frame(vFrame.mainWindow, padding=10)

        a = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start"))
        a.pack(pady=20)

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()