from codecs import backslashreplace_errors
from textwrap import fill
from tkinter import *
from tkinter import ttk
from turtle import color, width

class DisplayBoard:
    """Functions To Create a Playable board and Display Data to it"""

    boardColors = ["#8A5E3C","#CEBB8C"]
    letters = ['','a','b','c','d','e','f','']
    numbers = ['','6','5','4','3','2','1','']

    def __init__(self,vFrame):
        frame = Frame(vFrame, bg="#CEBB8C")
        
        x = 0
        y = 0
        colorBool = True
        while y < 8:
            while x < 8:
                doCanvas = True
                
                if y == 0 or y == 7 or x == 0 or x == 7:
                    doCanvas = False

                if x == 7 or x == 0 and y != 7 or y != 0:
                    Canvas(frame, bg=self.boardColors[0], height=1, width=1, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')

                if y == 0 and x != 0 and x != 7:
                    Canvas(frame, bg=self.boardColors[0], height=20, width=50, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=self.letters[x], bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False
                    
                if x == 0 and y != 0 and y != 7:
                    Canvas(frame, bg=self.boardColors[0], height=50, width=20, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=self.numbers[y], bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False

                if y == 7 and x != 0 and x != 7:
                    Canvas(frame, bg=self.boardColors[0], height=20, width=50, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=self.letters[x], bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False
                    
                if x == 7 and y != 0 and y != 7:
                    Canvas(frame, bg=self.boardColors[0], height=50, width=20, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y, sticky='ew ns')
                    Label(frame,text=self.numbers[y], bg=self.boardColors[0], fg= "white", font= ('Times 11 italic bold')).grid(column=x, row=y)
                    doCanvas = False



                if doCanvas is True:
                    Canvas(frame, bg=self.boardColors[int(colorBool)], height=50, width=50, bd=0, highlightthickness=0, relief='ridge').grid(column=x, row=y)
                    colorBool = not colorBool
                x = x + 1
            colorBool = not colorBool

            x = 0
            y = y + 1

        frame.grid(column=0, row=1, padx=1, pady=1)

    def on_click():
        print("HI")