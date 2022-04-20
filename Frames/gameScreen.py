from tkinter import *
from tkinter import ttk

class GameScreen:
    """Game Screen Content"""

    canvas = ""
    frame = ""

    cellSize = 50
    cellRows = 6

    colors = ["black", "white"]
    player_colors = ["red", "blue"]

    board = [
        [1,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,2,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
        ]

    def __init__(self,vFrame):
        self.frame = ttk.Frame(vFrame.mainWindow, padding=10)

        Button(self.frame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)

        self.updateCanvas()
        
        vFrame.mainWindow.frm = self.frame
        vFrame.mainWindow.frm.grid()

    def drawPlayer(self,frame):
        x = 0
        y = 0
        while y < self.cellRows:
            while x < self.cellRows:
                xs = x * self.cellSize
                ys = y * self.cellSize
                if self.board[y][x] != 0:
                    self.canvas.create_oval(xs, ys, xs + self.cellSize, ys + self.cellSize, fill=self.player_colors[self.board[y][x] - 1],width=0, tags="playerbutton")
                    self.canvas.tag_bind("playerbutton","<Button-1>", self.playerClicked)

                x = x + 1
            x = 0
            y = y + 1

    def playerClicked(self):
        self.board[3][3] = 2
        self.updateCanvas()
        
    def updateCanvas(self):
        self.drawBoard(self.frame)
        self.drawPlayer(self.frame)

    def drawBoard(self,frame):
        self.canvas = Canvas(frame, bg="white", height=self.cellSize*self.cellRows, width=self.cellSize*self.cellRows)
        self.canvas.config(highlightthickness=0)
        x = 0
        y = 0
        colorIndex = 0
        while y < self.cellRows:
            while x < self.cellRows:
                xs = x * self.cellSize
                ys = y * self.cellSize

                self.canvas.create_rectangle(xs, ys, xs + self.cellSize, ys + self.cellSize, fill=self.colors[colorIndex])

                colorIndex = colorIndex + 1
                if colorIndex == 2:
                    colorIndex = 0
                 
                x = x + 1

            colorIndex = colorIndex + 1
            if colorIndex == 2:
                colorIndex = 0

            x = 0
            y = y + 1
        self.canvas.grid(column=0,row=1,pady=5)

    
