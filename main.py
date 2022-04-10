#import tkinter as tkinter
from tkinter import *
from tkinter import ttk

#Beta InputCheck INT
def checkIntegerInput(input):
    try:
        val = int(input)
        # print("Eingabe ist eine Nummer. Wert = ", val)
    except ValueError:
        typeOfInput = input.type()
        print("Bitte geben Sie einen INTEGER ein. Ihre Eingabe war ein {}".format(typeOfInput))
        exit()


def main():
    mainWindow = Tk()
    mainWindow.title("Minimax Algorithm")
    #TODO: Percentage-based window size 30%?
    mainWindow.geometry("200x200")
    frm = ttk.Frame(mainWindow, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=mainWindow.destroy).grid(column=5, row=3)
    mainWindow.mainloop()


if __name__ == "__main__":
    main()