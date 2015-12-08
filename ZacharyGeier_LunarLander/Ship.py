from tkinter import *
from ShipShape import ShipShape
import math

class Ship:
    def __init__(self, canvas):
        self.x = 100
        self.y = 100
        self.r = 180
        self.center = self.x, self.y
        self.canvas = canvas
        self.thrust = True
        self.start = 0
        self.shapes = []
        self.scale = 5

        self.shipShape = ShipShape(self.x, self.y, self.scale, self.canvas)

    def update(self):
        self.shipShape = ShipShape(self.x, self.y, self.scale, self.canvas)

    def press(self, x, y):
        self.shipShape.press(x, y)

    def motion(self, x, y):
        self.shipShape.motion(x, y)

    def delete(self):
        self.shipShape.delete()