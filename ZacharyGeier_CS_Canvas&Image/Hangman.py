from tkinter import *

class HangmanGame:
    def __init__(self):
        window = Tk()

        canvas = Canvas(window, width=300, height=400)
        canvas.pack()

        canvas.create_line(150,125,150,200)
        canvas.create_line(150,200,100,250)
        canvas.create_line(150,200,200,250)
        canvas.create_line(150,200,100,250)
        canvas.create_line(150,150,100,200)
        canvas.create_line(150,150,200,200)
        canvas.create_oval(100,25,200,125)

        window.mainloop()

start = HangmanGame()