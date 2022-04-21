from tkinter import *
from tkinter import ttk
from Frames.gameScreen import GameScreen
from Frames.scoreboardScreen import ScoreBoardScreen
from Frames.selectDifficulty import SelectDifficulty
from Frames.startScreen import StartScreen
from Frames.settingsScreen import SettingsScreen

class VFrame:
    """Window Mangament Class"""

    """Initialize Screen"""
    global mainWindow
    global game

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title("Minimax Algorithm Python Games")
        self.mainWindow.geometry("900x900")
        self.mainWindow.resizable(True, True)

    """Clears Screen and Opens new Window"""
    def openScreen(self,text ,game = ""):
        if game != "" :
            self.game = game
            
        if hasattr(self.mainWindow, 'frm'):
            self.mainWindow.frm.destroy()

        if text == "start":
            StartScreen(self)
        if text == "difficulty":
            SelectDifficulty(self)
        if text == "game":
            GameScreen(self)
        if text == "scoreboard":
            ScoreBoardScreen(self)
        if text == "settings":
            SettingsScreen(self)
