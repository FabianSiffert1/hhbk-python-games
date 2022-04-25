from tkinter import *

from Game.movements import Movements
from Game.vector2 import Vector2

from Game.displayBoard import DisplayBoard
from Game.gameTable import GameTable
from Game.gameScore import GameScore

class Game:
    """Game Screen Content"""

    cellSize = 50
    cellCount = 6
    playerOneTeam = 1
    playerTwoTeam = 2


    global display
    global vFrame
    global frame
    global playerPositions
    global movableHighlights
    global selected
    global currentScore

    def __init__(self,vFrame):
        self.vFrame = vFrame
        self.frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        buttonFrame = Frame(self.frame, bg="#CEBB8C")

        Button(buttonFrame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)
        Button(buttonFrame, text="Restart Game", command= lambda: self.restart()).grid(column=1,row=0,sticky=W,padx=0,pady=0)
        Button(buttonFrame, text="Change Score", command=lambda: self.currentScore.evaluateScore(self.playerPositions, self.playerOneTeam, self)).grid(column=2, row=0, sticky=W, padx=0, pady=0)

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
            self.playerPositions = GameTable().chessPositions
        if self.vFrame.game == "dame":
            self.playerPositions = GameTable().checkersPositions
        self.currentScore = GameScore()

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
            print("team1: " + str( self.currentScore.evaluateScore(self.playerPositions, self.playerOneTeam, self.cellCount)))
            print("team2: " + str(  self.currentScore.evaluateScore(self.playerPositions, self.playerTwoTeam, self.cellCount)))
            #print(self.currentScore.evaluateScore(self.playerPositions, self.playerOneTeam, self))
           # print(self.currentScore.evaluateScore(self.playerPositions, self.playerTwoTeam, self))
            

    def selectFigure(self,x,y):
        #1  Blauer Punkt, 2 Roter Punkt, 0 Nichts / Auswahl, welche Farbe Spieler kontrolliert
        if self.playerPositions[y][x] == self.playerOneTeam or self.playerPositions[y][x] == self.playerTwoTeam:
            self.selected = Vector2(x,y)
            self.movableHighlights = self.getMovableFields(x,y)
        

    def getMovableFields(self,x1,y1):
        movable = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 

        if self.vFrame.game == "schach":
            self.movable = Movements().getMovableFieldsPawn(x1,y1,self.playerPositions,movable,self)
        if self.vFrame.game == "dame":
            self.movable = Movements().getMovableFieldsCheckers(x1,y1,self.playerPositions,movable,self)
        return movable