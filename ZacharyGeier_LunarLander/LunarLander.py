from Ship import Ship
from Landscape import Landscape
from tkinter import *
import math

class LunarLander:
    def __init__(self):
        window = Tk()
        window.title("Lunar Lander")

        self.canvas = Canvas(window, bg='black', width=500, height=400)
        self.canvas.pack()

        landscape = Landscape(self.canvas)
        self.ship = Ship(self.canvas)

        window.bind("<Left>", self.left)
        window.bind("<Right>", self.right)
        window.bind("<Up>", self.thrust)

        window.bind("<Button-1>", self.p)
        window.bind("<B1-Motion>", self.m)

        self.isStopped = False
        self.sleepTime = 100
        self.rad = 0
        self.updateLoop()

        window.mainloop()

    def updateLoop(self):
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.rad += .2
            self.canvas.update()

    def p(self, event):
        print(event.x,'\t', event.y)
        self.ship.press(event.x, event.y)

    def m(self, event):
        print(event.x,'\t',event.y)
        self.ship.motion(event.x, event.y, self.rad)

    def left(self, event):
        self.ship.press(1,0)
        self.ship.motion(1,0)

    def right(self, event):
        print(self.angle)
        self.ship.motion(math.cos(self.angle), math.sin(self.angle))

    def thrust(self, event):
        print('thrust')

start = LunarLander()