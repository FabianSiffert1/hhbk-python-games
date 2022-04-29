from tkinter import *
from tkinter import ttk
from Frames.game import Game
from Frames.scoreboardScreen import scoreBoardScreen
from Frames.selectDifficulty import selectDifficulty
from Frames.startScreen import startScreen
from Frames.settingsScreen import settingsScreen
from Frames.loginScreen import loginScreen
from Frames.gameEndScreen import GameEndScreen

class VFrame:
    """Window Mangament Class"""

    """Initialize Screen"""
    global mainWindow
    global game
    global username
    global database
    global winOrLossMessage

    def __init__(self):
        self.username = ""
        self.winOrLossMessage = "TEMP"
        self.mainWindow = Tk()
        self.mainWindow.title("Minimax Algorithm Python Games")
        self.mainWindow.geometry("400x400")
        self.mainWindow.resizable(True, True)
        self.mainWindow.configure(background='#CEBB8C')

    """Clears Screen and Opens new Window"""
    def openScreen(self,text ,game = ""):
        if game != "" :
            self.game = game
            
        if hasattr(self.mainWindow, 'frm'):
            self.mainWindow.frm.destroy()

        if text == "start":
            startScreen(self)
        if text == "difficulty":
            selectDifficulty(self)
        if text == "game":
            Game(self)
        if text == "scoreboard":
            scoreBoardScreen(self)
        if text == "settings":
            settingsScreen(self)
        if text == "login":
            loginScreen(self)
        if text == "gameEndScreen":
            GameEndScreen(self,game)
