from tkinter import *
from tkinter import ttk

class GameTable:
    """Game Screen Content"""

    global schachPositions
    global damePositions
    playerColors = ["blue","red"]
    def __init__(self):
        self.schachPositions = [
                [2,2,2,2,2,2],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,2,0,0,0],
                [1,1,1,1,1,1]
            ]

        self.damePositions = [
                [0,0,0,0,0,2],
                [2,0,2,0,2,0],
                [0,0,2,0,0,0],
                [0,0,0,2,0,0],
                [0,0,0,0,2,0],
                [1,1,1,1,1,1]
            ]

        

