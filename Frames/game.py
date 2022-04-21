from tkinter import *
from tkinter import ttk

from Game.displayBoard import DisplayBoard

class Game:
    """Game Screen Content"""

    playerPositions = [
            ['0','0','0','0','0','0'],
            ['0','1','0','0','0','0'],
            ['0','0','0','0','0','0'],
            ['0','0','0','0','0','0'],
            ['0','0','0','0','0','0'],
            ['0','0','0','0','0','1']
            ]

    def __init__(self,vFrame):
        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")
        Button(frame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)

        display = DisplayBoard(frame)
        
        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()

        display.updatePlayers(self.playerPositions)