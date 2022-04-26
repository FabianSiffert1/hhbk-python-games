import random
from tkinter import *

from Game.movements import Movements
from Game.vector2 import Vector2

from Game.displayBoard import DisplayBoard
from Game.gameTable import GameTable
from Game.gameScore import GameScore
from Game.artificialIntelligence import ArtificialIntelligence

class Game:
    """Game Screen Content"""

    cellSize = 50
    cellCount = 6
    playerOneTeam = 1
    playerTwoTeam = 2


    global display
    global vFrame
    global frame
    global figurePositions
    global movableHighlights
    global selected
    global currentScore
    global playerOneTurn
    global artificialIntelligenceEnabled

    def __init__(self,vFrame):
        self.vFrame = vFrame
        self.frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        buttonFrame = Frame(self.frame, bg="#CEBB8C")

        Button(buttonFrame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)
        Button(buttonFrame, text="Restart Game", command= lambda: self.restart()).grid(column=1,row=0,sticky=W,padx=0,pady=0)
        Button(buttonFrame, text="Change Turn", command=lambda: self.changeActivePlayer()).grid(column=2, row=0, sticky=W, padx=0, pady=0)

        buttonFrame.grid(column=0,row=0,sticky=W,padx=0,pady=0)

        self.display = DisplayBoard(self.frame,self)
        self.startNewGame()

        vFrame.mainWindow.frm = self.frame
        vFrame.mainWindow.frm.grid()

    def startNewGame(self):
        self.selected = Vector2(-1, -1)
        self.figurePositions = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)]
        self.movableHighlights = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 

        if self.vFrame.game == "schach":
            self.figurePositions = GameTable().chessPositions
            self.refreshScreen()
        if self.vFrame.game == "dame":
            self.figurePositions = GameTable().checkersPositions
            self.refreshScreen()
        self.currentScore = GameScore()
        #TODO: IMPLEMENT CHOOSING STARTING SITE ie. PlayerOne or PlayerTwo
        self.playerOneTurn = True
        #TODO: SETTINGS AI SWITCH
        self.artificialIntelligenceEnabled = True

    def restart(self):
        self.startNewGame()
        self.refreshScreen()

        
    def refreshScreen(self):
        self.display.clear()
        self.display.updatePlayers(self.figurePositions)
        self.display.updateMovableHighlights(self.movableHighlights)
        self.display.highlite(self.selected.x,self.selected.y)

    def fieldClicked(self,x,y):
        self.selectFigure(x,y)
        self.moveFigure(x,y)
        self.refreshScreen()

    def moveFigure(self,x1,y1):
        if self.movableHighlights[y1][x1] == 1:
            self.figurePositions[y1][x1] = self.figurePositions[self.selected.y][self.selected.x]
            self.figurePositions[self.selected.y][self.selected.x] = 0
            self.selected = Vector2(-1,-1)
            self.movableHighlights = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)]
            #print("team1: " + str( self.currentScore.evaluateScore(self.playerPositions, self.playerOneTeam, self.cellCount)))
            #print("team2: " + str(  self.currentScore.evaluateScore(self.playerPositions, self.playerTwoTeam, self.cellCount)))
            self.changeActivePlayer()
            if self.playerOneTurn == False and self.artificialIntelligenceEnabled == True:
                currentAITeam = self.getAITeam()
                #LOGIK: GET all movable pieces
                teamPieces = self.getAllTeamPieces(self.figurePositions, currentAITeam)
                # select random movable piece
                randomPiece = random.choice(teamPieces)
                print(randomPiece.x, randomPiece.y)
                # get movable fields
                self.getMovableFields(randomPiece.x, randomPiece.y)
                #print(self.getMovableFields(randomPiece.x, randomPiece.y))
                # move piece to movable field
                self.figurePositions[y1][x1] = self.figurePositions[self.selected.y][self.selected.x]
                self.figurePositions[randomPiece.y][randomPiece.x] = 0
                # set old position to 0 (remove old piece)
                #self.movable = self.getMovableFields(0,0)
                #print(self.movable)
                #figurePositionsAI = ArtificialIntelligence().takeTurn(self.figurePositions)
                #print("moving piece")
                #self.figurePositions[figurePositionsAI[0]][figurePositionsAI[1]] = currentAITeam
                self.changeActivePlayer()
                print("End of AI Turn")
                self.refreshScreen()

            #TODO: IMPLEMENT PLAYER 2 CONTROLS
            #if self.playerOneTurn == False and self.artificialIntelligenceEnabled == False:
                #PlayerTwo Turn
                #Implement Turn Indicator

    def changeActivePlayer(self):
        self.playerOneTurn = not self.playerOneTurn

    #TODO: IMPLEMENT AI Team Switch
    def getAITeam(self):
        return self.playerTwoTeam

    def selectFigure(self,x,y):
        #1  Blauer Punkt, 2 Roter Punkt, 0 Nichts / Auswahl, welche Farbe Spieler kontrolliert
        if self.figurePositions[y][x] == self.playerOneTeam and self.playerOneTurn == True:
            self.selected = Vector2(x,y)
            self.movableHighlights = self.getMovableFields(x,y)

        
    def getAllTeamPieces (self, figurePositions, team):
        x = 0
        y = 0
        teamPieces = []
        while x < self.cellCount:
            while y < self.cellCount:
                if figurePositions[y][x] == team:
                    teamPieces.append(Vector2(x,y))
                y += 1
            y = 0
            x += 1
        return teamPieces

    def getMovableFields(self,x1,y1):
        movable = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)] 

        if self.vFrame.game == "schach":
            self.movable = Movements().getMovableFieldsChess(x1, y1, self.figurePositions, movable, self)
        if self.vFrame.game == "dame":
            self.movable = Movements().getMovableFieldsCheckers(x1, y1, self.figurePositions, movable, self)
        return movable