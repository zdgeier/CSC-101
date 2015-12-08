from tkinter import *
import math


class ShipShape:
    def __init__(self, x, y, scale, canvas):
        self.shapes = []
        self.shapesXY = []
        self.x = x
        self.y = y
        self.center = self.x, self.y
        self.canvas = canvas
        self.color = 'white'
        self.angle = 0

        scale2 = scale*2

        x1 = self.x+scale; x2 = self.x+scale2
        y1 = self.y+scale; y2 = self.y+scale2
        x3 = self.x-scale; x4 = self.x-scale2
        y3 = self.y-scale; y4 = self.y-scale2

        y5 = self.y+scale2+scale
        y6 = self.y+scale2+scale2

        #Octogon
        oct = [(x1,y2),(x2,y1),(x2,y3),(x1,y4),(x3,y4),(x4,y3),(x4,y1),(x3,y2)]
        body = self.canvas.create_polygon(oct, fill=self.color, tag='body')
        self.shapesXY.append(oct)
        self.shapes.append(body)

        #Trapezoid
        trap = [(x1,y2),(x2,y5),(x4,y5),(x3,y2)]
        engine = self.canvas.create_polygon(trap, fill=self.color, tag='engine')
        self.shapesXY.append(trap)
        self.shapes.append(engine)

        #Triangle
        tri = [(x1,y5),(self.x,y6),(x3,y5)]
        thrust = self.canvas.create_polygon(tri, fill=self.color, tag='thrust')
        self.shapesXY.append(tri)
        self.shapes.append(thrust)

    def getangle(self, x, y):
        dx = x - self.center[0]
        dy = y - self.center[1]
        try:
            return complex(dx, dy) / abs(complex(dx, dy))
        except ZeroDivisionError:
            return 0.0 # cannot deterscalee angle

    def press(self, x, y):
        # calculate angle at start point
        self.start = self.getangle(x, y)

    def motion(self, x, y):
        # calculate current angle relative to initial angle
        angle = self.getangle(x, y) / self.start
        offset = complex(self.center[0], self.center[1])
        newcenter = []
        shapeIndex = 0
        for shapeXY in self.shapesXY:
            for x, y in shapeXY:
                v = angle * (complex(x, y) - offset) + offset
                newcenter.append(v.real)
                newcenter.append(v.imag)
            self.canvas.coords(self.shapes[shapeIndex], *newcenter)
            shapeIndex += 1