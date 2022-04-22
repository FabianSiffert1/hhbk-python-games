from tkinter import *
from tkinter import ttk
from Game.movements import Movements
from Game.vector2 import Vector2

from Game.displayBoard import DisplayBoard
from Game.gameTable import GameTable

class Game:
    """Game Screen Content"""

    cellSize = 50
    cellCount = 6


    global display
    global vFrame
    global frame
    global playerPositions
    global movableHighlights
    global selected

    def __init__(self,vFrame):
        self.vFrame = vFrame
        self.frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        buttonFrame = Frame(self.frame, bg="#CEBB8C")

        Button(buttonFrame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)
        Button(buttonFrame, text="RestartGame", command= lambda: self.restart()).grid(column=1,row=0,sticky=W,padx=0,pady=0)

        buttonFrame.grid(column=0,row=0,sticky=W,padx=0,pady=0)

        self.display = DisplayBoard(self.frame,self)
        self.startNewGame()

        vFrame.mainWindow.frm = self.frame
        vFrame.mainWindow.frm.grid()

    def startNewGame(self):
        self.selected = Vector2(-1, -1)
        self.playerPositions = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 
        self.movableHighlights = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 

        if self.vFrame.game == "schach":
            self.playerPositions = GameTable.schachPositions
        if self.vFrame.game == "dame":
            self.playerPositions = GameTable.damePositions

        self.refreshScreen()

    def restart(self):
        self.startNewGame()
        self.refreshScreen()

        
    def refreshScreen(self):
        self.display.clear()
        self.display.updatePlayers(self.playerPositions)
        self.display.updateMovableHighlights(self.movableHighlights)
        self.display.highlite(self.selected.x,self.selected.y)

    def fieldClicked(self,x,y):
        self.selectFigure(x,y)
        self.moveFigure(x,y)
        self.refreshScreen()

    def moveFigure(self,x1,y1):
        if self.movableHighlights[y1][x1] == 1:
            self.playerPositions[y1][x1] = self.playerPositions[self.selected.y][self.selected.x]
            self.playerPositions[self.selected.y][self.selected.x] = 0
            self.selected = Vector2(-1,-1)
            self.movableHighlights = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 
            

    def selectFigure(self,x,y):
        if self.playerPositions[y][x] == 1:
            self.selected = Vector2(x,y)
            self.movableHighlights = self.getMovableFields(x,y)
        

    def getMovableFields(self,x1,y1):
        movable = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 

        if self.vFrame.game == "schach":
            self.movable = Movements().getMovableFieldsPawn(x1,y1,self.playerPositions,movable,self)
        if self.vFrame.game == "dame":
            self.movable = Movements().getMovableFieldsCheckers(x1,y1,self.playerPositions,movable,self)

        return movable