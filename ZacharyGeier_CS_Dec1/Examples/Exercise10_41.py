from tkinter import * # Import tkinter
import math

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        return
    
    # Is point (x, y) inside this circle?
    def isInside(self, x, y):
        return distance(self.x, self.y, x, y) <= self.radius
    
    def __str__(self):
        return self.color

def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

width = 400
height = 250
x = 100
y = 100
hGap = 120
vGap = 50
radius = 50
          
class MainGUI:
    def __init__(self):      
        window = Tk() # Create a window
        window.title("Olympic Symbol") # Set title

        self.canvas = Canvas(window, width = width, height = height)
        self.canvas.pack()
        
        c1 = Circle(x, y, radius, "blue")
        c2 = Circle(x + hGap, y, radius, "black")
        c3 = Circle(x + 2 * hGap, y, radius, "red")
        c4 = Circle(x + radius, y + vGap, radius, "yellow")
        c5 = Circle(x + 190 , y + vGap, radius, "green")
        self.circles = [c1, c2, c3, c4, c5]
        self.paint(self.circles)
        
        self.canvas.bind("<B1-Motion>", self.mouseMoved)
        
        window.mainloop() # Create an event loop
        return
        
    def mouseMoved(self, event):
        for c in self.circles:
            if c.isInside(event.x, event.y):
                c.x = event.x
                c.y = event.y
                self.canvas.delete(str(c))
                self.paintCircle(c)
                break
        return
    
    def paintCircle(self, c):
        self.canvas.create_oval(c.x - c.radius, c.y - c.radius, c.x + c.radius, c.y + c.radius, fill = c.color, tags = str(c))
        return
    
    def paint(self, circles):
        for c in self.circles:
            self.paintCircle(c)    
        return
    
MainGUI()
