from codecs import backslashreplace_errors
from textwrap import fill
from tkinter import *
from tkinter import ttk

from Game.gameTable import GameTable
from Game.vector2 import Vector2

class DisplayBoard:
    """Functions To Create a Playable board and Display Data to it"""

    boardColors = ["#8A5E3C","#CEBB8C"]
    letters = ['','a','b','c','d','e','f', 'g' , 'h', 'i' , 'j', 'k' , 'l', 'm' ,'n','o','p','q','r','s','t','u','v','w','x','y','z' ,'']

    global canvases
    global game

    def __init__(self,vFrame,game):
        self.game = game
        frame = Frame(vFrame, bg="#CEBB8C")
        self.canvases = [[0 for x in range(game.cellCount)] for y in range(game.cellCount)] 
        
        x = 0
        y = 0
        colorBool = True

        while y < game.cellCount + 2: 
            while x < game.cellCount + 2:
                doCanvas = True
                
                if y == 0 or y == game.cellCount + 1 or x == 0 or x == game.cellCount + 1:
                    doCanvas = False

                if x == game.cellCount + 1 or x == 0 and y != game.cellCount + 1 or y != 0:
                    Canvas(frame, bg=self.boardColors[0], height=1, width=1, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')

                if y == 0 and x != 0 and x != game.cellCount + 1:
                    Canvas(frame, bg=self.boardColors[0], height=20, width=50, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=self.letters[x], bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False
                    
                if x == 0 and y != 0 and y != game.cellCount + 1:
                    Canvas(frame, bg=self.boardColors[0], height=50, width=20, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=game.cellCount - y + 1, bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False

                if y == game.cellCount + 1 and x != 0 and x != game.cellCount + 1:
                    Canvas(frame, bg=self.boardColors[0], height=20, width=50, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=self.letters[x], bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False
                    
                if x == game.cellCount + 1 and y != 0 and y != game.cellCount + 1:
                    Canvas(frame, bg=self.boardColors[0], height=50, width=20, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=game.cellCount - y + 1, bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False

                if doCanvas is True:
                    canv = Canvas(frame, bg=self.boardColors[int(colorBool)], height=50, width=50, bd=0, highlightthickness=0)
                    canv.bind("<ButtonRelease-1>", 
                        lambda event, a=x - 1, b=y - 1: 
                            self.fieldClicked(a, b))
                    canv.grid(column=x, row=y)
                    self.canvases[y - 1][x - 1] = canv
                    
                    colorBool = not colorBool
                x = x + 1
            colorBool = not colorBool

            x = 0
            y = y + 1

        frame.grid(column=0, row=1, padx=1, pady=1)

    def fieldClicked(self, x, y):
        """Select Figure"""
        self.game.fieldClicked(x,y)

    def highlite(self, x, y):
        if x != -1 and y != -1:
            self.canvases[y][x].create_rectangle(0,0,self.game.cellSize - 1, self.game.cellSize - 1,outline="#FFD700", width=2)

    def clear(self):
        for x in range(self.game.cellCount):
            for y in range(self.game.cellCount):
                self.canvases[x][y].delete("all")

    def updatePlayers(self,playerPositions):
        for x in range(self.game.cellCount):
            for y in range(self.game.cellCount):
                if playerPositions[x][y] != 0:
                    self.canvases[x][y].create_oval(5, 5, self.game.cellSize - 5, self.game.cellSize - 5, fill=GameTable.playerColors[playerPositions[x][y] - 1], outline="") 

    def updateMovableHighlights(self,movableHighlights):
        for x in range(self.game.cellCount):
            for y in range(self.game.cellCount):
                if movableHighlights[x][y] != 0:
                    self.canvases[x][y].create_oval(15, 15, self.game.cellSize - 15, self.game.cellSize - 15, fill="grey", outline="") 
