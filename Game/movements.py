from codecs import backslashreplace_errors
from math import fabs
import sys
from textwrap import fill
from tkinter import *
from tkinter import ttk

from Game.gameTable import GameTable

class Movements:
    """Functions for movement"""

    def insideBounds(self,x,y,game):
        if x < 0 or x >= game.cellCount:
            return False
        if y < 0 or y >= game.cellCount:
            return False
        return True
            

    def getMovableFieldsChess(self, x, y, player, moveable, game):
        
        if self.insideBounds(x,y,game):
            team = player[y][x]
            direction = (team - 1) * 2 - 1

        if self.insideBounds(x,y+direction,game):
            if player[y+direction][x] == 0:
                moveable[y+direction][x] = 1


        if self.insideBounds(x-1,y+direction,game):
            if player[y+direction][x-1] != team and player[y+direction][x-1] != 0:
                moveable[y+direction][x-1] = 1

        if self.insideBounds(x+1,y+direction,game):
            if player[y+direction][x+1] != team and player[y+direction][x+1] != 0:
                moveable[y+direction][x+1] = 1

        return moveable



    def getMovableFieldsCheckers (self,x,y,player,moveable,game):
        if self.insideBounds(x,y,game):
            team = player[y][x]
            directionY = (team - 1) * 2 - 1
            i = 1
            moveable = self.CheckersIterate(x,y,1,directionY,i,player,moveable,game,team)
            moveable = self.CheckersIterate(x,y,-1,directionY,i,player,moveable,game,team)

        
        return moveable

    def CheckersIterate (self,x,y,directionX,directionY,i,player,moveable,game,team,canJump = True,jumpedOverEnemy = False, jumpCounter = 0):
        if x+(directionX*i) < 0:
            return moveable
        if not self.insideBounds(x+(directionX*i),y+(directionY*i),game):
            return moveable
        if player[y+(directionY*i)][x+(directionX*i)] != team:
            if player[y+(directionY*i)][x+(directionX*i)] == 0:
                if canJump is True and jumpCounter < 1:
                    moveable[y+(directionY*i)][x+(directionX*i)] = 1
                    if jumpedOverEnemy is True:
                        self.CheckersIterate(x,y,directionX,directionY,i + 1,player,moveable,game,team,True,False, jumpCounter+1)
                    else:
                        self.CheckersIterate(x,y,directionX,directionY,i + 1,player,moveable,game,team,False,False,0)
            else:
                if jumpedOverEnemy is False and canJump == True:
                    self.CheckersIterate(x,y,directionX,directionY,i + 1,player,moveable,game,team,True,True)
                
        
        return moveable

