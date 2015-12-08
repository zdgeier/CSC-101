from tkinter import *
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        return

    # Is point (x, y) inside this circle?
    def isInside(self, x, y):
        return distance(self.x, self.y, x, y) <= self.radius

def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

def KeyLeftRight(event):
    global x1,y1,x2,y2
    if event.keysym == 'Left':
        canvas.delete('circle')
        x1 -= 2
        x2 -= 2
        canvas.create_oval(x1, y1, x2, y2, tags = 'circle')
    elif event.keysym == 'Right':
        canvas.delete('circle')
        x1 += 2
        x2 += 2
        canvas.create_oval(x1, y1, x2, y2, tags = 'circle')
    return

def MouseClick(event):
    global x1,y1,x2,y2,mouseState
    mouseState = 'Down'
    return

def mouseMoved(event):
    global x1,y1,x2,y2,mouseState
    if mouseState == 'Down':
        if c.isInside(event.x, event.y):
            c.x = event.x
            c.y = event.y
            canvas.delete('circle')
            paintCircle(c)

def paintCircle(c):
    canvas.create_oval(c.x - c.radius, c.y - c.radius, c.x + c.radius, c.y + c.radius, fill='white', tags='circle')
    return

window = Tk()

canvas = Canvas(window, width = 300, height = 300)
canvas.pack()

x1 = 150
y1 = 150
radius = 50

mouseState = 'Up'

c = Circle(x1, y1, radius)
paintCircle(c)

canvas.focus_set()

canvas.bind("<Button-1>", MouseClick)
canvas.bind("<B1-Motion>", mouseMoved)

window.mainloop()
