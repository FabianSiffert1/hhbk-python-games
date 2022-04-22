from tkinter import *
from tkinter import ttk

class GameTable:
    """Game Screen Content"""

    schachPositions = [
            [2,2,2,2,2,2],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,2,0,0,0],
            [1,1,1,1,1,1]
        ]

    damePositions = [
            [0,0,0,0,0,2],
            [2,0,2,0,2,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,1,0,1,0,1],
            [1,0,1,0,1,0]
        ]

    playerColors = ["blue","red"]
        

