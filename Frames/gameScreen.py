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
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
        ]

    startBauer = [
        [2,2,2,2,2,2],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [1,1,1,1,1,1]
        ]
    
    startDame = [
        [0,2,0,2,0,2],
        [2,0,2,0,2,0],
        [0,0,0,0,0,0],
        [0,0,0,0,2,0],
        [0,1,0,1,0,1],
        [1,0,1,0,1,0]
        ]

    selectedX = -1
    selectedY = -1

    global vFrame

    def __init__(self,vFrame):
        self.vFrame = vFrame
        if vFrame.game == "schach":
            self.board = self.startBauer
        if vFrame.game == "dame":
            self.board = self.startDame
        self.frame = ttk.Frame(vFrame.mainWindow, padding=10)

        Button(self.frame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)

        self.updateCanvas()
        
        vFrame.mainWindow.frm = self.frame
        vFrame.mainWindow.frm.grid()

        

    def drawPlayer(self):
        x = 0
        y = 0
        while y < self.cellRows:
            while x < self.cellRows:
                xs = x * self.cellSize
                ys = y * self.cellSize
                if self.board[y][x] != 0:
                    self.canvas.create_oval(xs, ys, xs + self.cellSize - 1, ys + self.cellSize - 1, fill=self.player_colors[self.board[y][x] - 1],width=0, tags="playerbutton")
                    self.canvas.tag_bind("playerbutton","<ButtonPress-1>", self.playerClicked)

                x = x + 1
            x = 0
            y = y + 1

    def playerClicked(self,clicked):
        self.fieldClicked(clicked)
        
        x = int(clicked.x / self.cellSize)
        y = int(clicked.y / self.cellSize)

        self.updateCanvas()

        if self.selectedX == -1 :
            self.selectedX = x
            self.selectedY = y
            self.highliteField()
            if self.vFrame.game == "schach":
                self.markFieldMovableSchach()
            if self.vFrame.game == "dame":
                self.markFieldMovableDame()
            self.drawPlayer()
            
        else:
            self.selectedX = -1
            self.selectedY = -1

    def fieldClicked(self,clicked):
        x = int(clicked.x / self.cellSize)
        y = int(clicked.y / self.cellSize)
        playerType = self.board[self.selectedY][self.selectedX]
        playerType2 = self.board[y][x]

        if self.selectedX != -1:
            if playerType2 != playerType:
                self.board[self.selectedY][self.selectedX] = 0
                self.board[y][x] = playerType
                self.selectedX = -1
                self.selectedY = -1
        
        self.updateCanvas()
        self.highliteField()
        if self.vFrame.game == "schach":
            self.markFieldMovableSchach()
        if self.vFrame.game == "dame":
            self.markFieldMovableDame()
        self.drawPlayer()

    def updateCanvas(self):
        self.drawBoard()
        self.drawPlayer()

    def highliteField(self):
        xs = self.selectedX * self.cellSize
        ys = self.selectedY * self.cellSize
        self.canvas.create_rectangle(xs, ys, xs + self.cellSize, ys + self.cellSize, outline="red",width=2)

    def markFieldMovableDame(self):
        try:
            xs = (self.selectedX - 1) * self.cellSize
            ys = (self.selectedY - 1) * self.cellSize

            if self.board[self.selectedY - 1][self.selectedX - 1] == 0:
                self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
            else:
                xs = (self.selectedX - 2) * self.cellSize
                ys = (self.selectedY - 2) * self.cellSize
                if self.board[self.selectedY - 2][self.selectedX - 2] == 0:
                    self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                    self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
        except:
            print("Out Of Range")

        try:
            xs = (self.selectedX + 1) * self.cellSize
            ys = (self.selectedY - 1) * self.cellSize

            if self.board[self.selectedY - 1][self.selectedX + 1] == 0:
                self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
            else:
                xs = (self.selectedX + 2) * self.cellSize
                ys = (self.selectedY - 2) * self.cellSize
                if self.board[self.selectedY - 2][self.selectedX + 2] == 0:
                    self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                    self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
        except:
            print("Out Of Range")

    def markFieldMovableSchach(self):
        try:
            xs = (self.selectedX) * self.cellSize
            ys = (self.selectedY - 1) * self.cellSize

            if self.board[self.selectedY - 1][self.selectedX] == 0:
                self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
        except:
            print("Out Of Range")

        try:
            xs = (self.selectedX - 1) * self.cellSize
            ys = (self.selectedY - 1) * self.cellSize

            if self.board[self.selectedY - 1][self.selectedX - 1] != 0:
                self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
        except:
            print("Out Of Range")

        try:
            xs = (self.selectedX + 1) * self.cellSize
            ys = (self.selectedY - 1) * self.cellSize

            if self.board[self.selectedY - 1][self.selectedX + 1] != 0:
                self.canvas.create_rectangle(xs + 2, ys + 2, xs + self.cellSize - 2, ys + self.cellSize - 2, fill="yellow",width=0, tags="fieldButton")
                self.canvas.tag_bind("fieldButton","<ButtonPress-1>", self.fieldClicked)
        except:
            print("Out Of Range")

    def drawBoard(self):
        self.canvas = Canvas(self.frame, bg="white", height=self.cellSize*self.cellRows, width=self.cellSize*self.cellRows)
        self.canvas.config(highlightthickness=0)
        x = 0
        y = 0
        colorIndex = 0
        while y < self.cellRows:
            while x < self.cellRows:
                xs = x * self.cellSize
                ys = y * self.cellSize

                self.canvas.create_rectangle(xs, ys, xs + self.cellSize, ys + self.cellSize, fill=self.colors[colorIndex],width=0)

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

