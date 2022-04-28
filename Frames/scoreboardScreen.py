from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3

class scoreBoardScreen:
    """Scoreboard Screen Content"""

    def __init__(self,vFrame):
        frame = Frame(vFrame.mainWindow, bg="#CEBB8C")

        quitButton = Button(frame, text="Exit", command= lambda: vFrame.openScreen("start"))
        quitButton.grid(column=0,row=0,padx=5,pady=2.5)

        """testText = tkinter.Label(frame, text="Test")
        testText.pack()"""

        

        """height = 10
        for c in range(height):
            scoreboardSpalteName = tkinter.Label(frame, text="Name")
            scoreboardSpaltePunkte = tkinter.Label(frame, text="Punkte")
            scoreboardSpalteName.grid(column=1,row=c + 1,padx=5,pady=2.5, ipadx=10)
            scoreboardSpaltePunkte.grid(column=2,row=c + 1,padx=5,pady=2.5, ipadx=10)"""

        game = ""      # 0 = Schach, 1 = Dame

        quitButton = Button(frame, text="Bauer", command= lambda: self.scoreboardView(frame, 0))
        quitButton.grid(column=10,row=0,padx=5,pady=2.5)

        quitButton = Button(frame, text="Dame", command= lambda: self.scoreboardView(frame, 1))
        quitButton.grid(column=20,row=0,padx=5,pady=2.5)        

        vFrame.mainWindow.frm = frame
        vFrame.mainWindow.frm.grid()
    

    def scoreboardView(self, frame, game):
        db = sqlite3.connect("Scoreboard.db")
        c = db.cursor()

        c.execute("SELECT username, score FROM scoreboard  WHERE game = ? ORDER BY score DESC LIMIT 10", (game,))
        rows = c.fetchall()

        countRow = 2
        scoreboardSpalteName = tkinter.Label(frame, text="Name")
        scoreboardSpaltePunkte = tkinter.Label(frame, text="Punkte")
        scoreboardSpalteName.grid(column=1,row=countRow,padx=5,pady=2.5, ipadx=10)
        scoreboardSpaltePunkte.grid(column=2,row=countRow,padx=5,pady=2.5, ipadx=10)
        for row in rows:
            scoreboardSpalteName = tkinter.Label(frame, text=row[0])
            scoreboardSpaltePunkte = tkinter.Label(frame, text=row[1])
            scoreboardSpalteName.grid(column=1,row=countRow + 1,padx=5,pady=2.5, ipadx=10)
            scoreboardSpaltePunkte.grid(column=2,row=countRow + 1,padx=5,pady=2.5, ipadx=10)

            countRow += 1
            #print(row[0])