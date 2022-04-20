from tkinter import *
from tkinter import ttk

class GameScreen:
    """Game Screen Content"""

    global vFrame

    cellSize = 50
    cellRows = 6

    colors = ["black", "white"]

    def __init__(self,vFrame):
        frame = ttk.Frame(vFrame.mainWindow, padding=10)

        button = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start")).grid(column=0,row=0,sticky=W,padx=0,pady=0)


        self.drawBoard(frame)

        

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()

       


    def drawBoard(self,frame):
        myCanvas = Canvas(frame, bg="white", height=self.cellSize*self.cellRows, width=self.cellSize*self.cellRows)
        myCanvas.config(highlightthickness=0)
        x = 0
        y = 0
        colorIndex = 0
        while y < self.cellRows:
            while x < self.cellRows:
                xs = x * self.cellSize
                ys = y * self.cellSize

                myCanvas.create_rectangle(xs, ys, xs + self.cellSize, ys + self.cellSize, fill=self.colors[colorIndex])

                colorIndex = colorIndex + 1
                if colorIndex is 2:
                    colorIndex = 0
                 
                x = x + 1

            colorIndex = colorIndex + 1
            if colorIndex is 2:
                colorIndex = 0

            x = 0
            y = y + 1
        myCanvas.grid(column=0,row=1,pady=5)

    
