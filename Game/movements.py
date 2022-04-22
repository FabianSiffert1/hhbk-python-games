from codecs import backslashreplace_errors
from textwrap import fill
from tkinter import *
from tkinter import ttk

from Game.gameTable import GameTable

class Movements:
    """Functions for movement"""

    def getMovableFieldsPawn(self,x,y,player,moveable,game):
        try:
            team = player[y][x]
            direction = (team - 1) * 2 - 1
        except:
            """"""
        try:
            if player[y+direction][x] == 0:
                moveable[y+direction][x] = 1
        except:
            """"""

        try:
            if player[y+direction][x-1] != team and player[y+direction][x-1] != 0:
                moveable[y+direction][x-1] = 1
        except:
            """"""
        try:
            if player[y+direction][x+1] != team and player[y+direction][x+1] != 0:
                moveable[y+direction][x+1] = 1
        except:
            """"""

        return moveable



    def getMovableFieldsCheckers (self,x,y,player,moveable,game):
        try:
            team = player[y][x]
            directionY = (team - 1) * 2 - 1
            i = 1
        except:
            """"""
        try:
            directionX = 1
            moveable = self.CheckersIterate(self,x,y,directionX,directionY,i,player,moveable,game,team)
        except:
            """"""
        try:
            directionX = -1
            moveable = self.CheckersIterate(self,x,y,directionX,directionY,i,player,moveable,game,team)
        except:
            """"""
        
        return moveable

    def CheckersIterate (self,x,y,directionX,directionY,i,player,moveable,game,team):

        if player[y+(directionY*i)][x+(directionX*i)] != team:
            if player[y+(directionY*i)][x+(directionX*i)] == 0:
                moveable[y+(directionY*i)][x+(directionX*i)] = 1

        
        return moveable

