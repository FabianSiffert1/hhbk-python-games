import random
import time
from tkinter import *
from copy import deepcopy
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
    global gameOver
    global winningTeam

    def __init__(self,vFrame):
        self.vFrame = vFrame
        self.frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        buttonFrame = Frame(self.frame, bg="#CEBB8C")

        Button(buttonFrame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)
        Button(buttonFrame, text="Restart Game", command= lambda: self.restart()).grid(column=1,row=0,sticky=W,padx=0,pady=0)

        buttonFrame.grid(column=0,row=0,sticky=W,padx=0,pady=0)

        self.display = DisplayBoard(self.frame,self)
        self.startNewGame()

        vFrame.mainWindow.frm = self.frame
        vFrame.mainWindow.frm.grid()

        #vFrame.database.insertScoreboard("TestUser", 123, 0)

    def startNewGame(self):
        self.gameOver = False
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
        self.checkWin()
        if self.gameOver is False:
            self.refreshScreen()

    def checkWin(self):
        x = 0
        y = 0
        while x < self.cellCount:
            while y < self.cellCount:
                if y == 0:
                    if self.figurePositions[y][x] == 1:
                        self.gameOver = True
                        self.winningTeam = 1

                if y == 5:
                    if self.figurePositions[y][x] == 2:
                        self.gameOver = True
                        self.winningTeam = 2
                y += 1
            y = 0
            x += 1
        if self.gameOver == True:
            #TODO: calculate Score
            #TODO: if logged in write score to leaderboard
            if self.winningTeam == self.getPlayerOneTeam():
                self.vFrame.winOrLossMessage = "You Won!"
                self.vFrame.openScreen("gameEndScreen", self.vFrame.game)
            else:
                self.vFrame.winOrLossMessage = "You Lost :("
                self.vFrame.openScreen("gameEndScreen", self.vFrame.game)

    def moveAiFigure(self,figurePositions,x1,y1,x2,y2):
        figurePositions[y2][x2] = figurePositions[y1][x1]
        figurePositions[y1][x1] = 0
        return figurePositions

    def miniMax1D(self):
        aiFigures = self.getAllTeamPieces(self.figurePositions, 2)
        #TODO: BUGFIX! Sometimes a piece that can not move is selected which crashes the AI
        playerScore = GameScore().evaluateScore(self.figurePositions,1,self.cellCount)
        move1 = Vector2(-1,-1)
        figureResult1 = Vector2(-1,-1)
        
        aiScore = GameScore().evaluateScore(self.figurePositions,2,self.cellCount)
        move2 = Vector2(-1,-1)
        figureResult2 = Vector2(-1,-1)
        
        for aifigure in aiFigures:
            movableFields = self.convertMovableField(self.getMovableFields(aifigure.x, aifigure.y))
            for field in movableFields:
                tempPositions = deepcopy(self.figurePositions)
                tempPositions = self.moveAiFigure(tempPositions,aifigure.x,aifigure.y,field.x,field.y)

                tempPlayerScore = GameScore().evaluateScore(tempPositions,1,self.cellCount)
                #print("playerScore"+ str(tempPlayerScore))
                if playerScore > tempPlayerScore:
                    move1 = field
                    figureResult1 = aifigure
                
                tempAiScore = GameScore().evaluateScore(tempPositions,2,self.cellCount)
                if aiScore < tempAiScore:
                    move2 = field
                    figureResult2 = aifigure
        #randomMove = random.choice(movableFields)
        if move1.x == -1:
            if move2.x == -1:
                print("shiot")
            else:
                self.moveAiFigure(self.figurePositions,figureResult2.x,figureResult2.y,move2.x,move2.y)
                if self.vFrame.game == "dame":
                    self.killJumpedEnemies(figureResult2.x, figureResult2.y, move2.x, move2.y)
        else:
            self.moveAiFigure(self.figurePositions,figureResult1.x,figureResult1.y,move1.x,move1.y)
            if self.vFrame.game == "dame":
                self.killJumpedEnemies(figureResult1.x, figureResult1.y, move1.x, move1.y)

    def killJumpedEnemies(self,oldPositionX, oldPositionY, newPositionX, newPositionY):
        if (abs(oldPositionX - newPositionX) > 1 or abs(oldPositionY - newPositionY) > 1):
            xPositionToKill = max(oldPositionX,newPositionX) - 1
            yPositionToKill = max(oldPositionY, newPositionY) - 1
            self.figurePositions[yPositionToKill][xPositionToKill] = 0
            #print("Killing: ["+ str(xPositionToKill+1) + "] [" + str(yPositionToKill+1) + "]")

    def moveFigure(self,x1,y1):
        if self.movableHighlights[y1][x1] == 1:
            self.figurePositions[y1][x1] = self.figurePositions[self.selected.y][self.selected.x]
            self.figurePositions[self.selected.y][self.selected.x] = 0
            if self.vFrame.game == "dame":
                self.killJumpedEnemies(x1,y1,self.selected.x, self.selected.y)
            self.selected = Vector2(-1,-1)
            self.movableHighlights = [[0 for x in range(self.cellCount)] for y in range(self.cellCount)]
            self.changeActivePlayer()
            self.refreshScreen()
            if self.playerOneTurn == False and self.artificialIntelligenceEnabled == True:
                currentAITeam = self.getAITeam()
                self.miniMax1D()
                #print(randomMove.x, randomMove.y)
                
                self.changeActivePlayer()
                #print("End of AI Turn")
                self.refreshScreen()
            #TODO: Print Current Score Funktion auslagern
            #print("team1: " + str( self.currentScore.evaluateScore(self.figurePositions, self.playerOneTeam, self.cellCount)))
            #print("team2: " + str(  self.currentScore.evaluateScore(self.figurePositions, self.playerTwoTeam, self.cellCount)))

            #TODO: IMPLEMENT PLAYER 2 CONTROLS
            #if self.playerOneTurn == False and self.artificialIntelligenceEnabled == False:
                #PlayerTwo Turn
                #Implement Turn Indicator
                

    def changeActivePlayer(self):
        self.playerOneTurn = not self.playerOneTurn

    #TODO: Implement player controlled Team Switch
    def getPlayerOneTeam(self):
        return self.playerOneTeam

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

    def convertMovableField(self, movableFields):
        x = 0
        y = 0
        movableFieldsCoordinates = []
        while x < self.cellCount:
            while y < self.cellCount:
                if movableFields[y][x] == 1:
                   movableFieldsCoordinates.append(Vector2(x,y))
                y += 1
            y = 0
            x += 1
        return movableFieldsCoordinates