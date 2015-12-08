from tkinter import * # Import tkinter

  
class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Inside the circle?") # Set a title
        
        self.canvas = Canvas(window, bg = "white", width = 240, height = 120)
        self.canvas.pack()
        self.canvas.create_oval(100 - 50, 60 - 50, 100 + 50, 60 + 50, tags = "circle")
        
        self.canvas.bind("<B1-Motion>", self.isInside)
        
        window.mainloop() # Create an event loop
        
    def isInside(self, event):
        if isInsideCircle(100, 60, 50, event.x, event.y):
            print("Mouse pointer is in the circle")
        else:
            print("Mouse pointer is not in the circle")

def isInsideCircle(xCenter, yCenter, radius, x, y):
    isIn = (((xCenter - x) * (xCenter - x) + (yCenter - y) * (yCenter - y)) ** 0.5 <= radius)
    return isIn
    


MainGUI()
