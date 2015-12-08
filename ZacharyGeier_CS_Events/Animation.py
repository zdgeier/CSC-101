from tkinter import *

class Animation:
    def __init__(self):
        window = Tk()
        
        self.width = 300
        self.height = 300

        self.canvas = Canvas(window, self.width, self.height)
        self.canvas.pack()
        
        self.x1 = 100
        self.y1 = 100
        self.x2 = 200
        self.y2 = 200
        
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags = 'circle')
        
        self.canvas.bind("<Key>", self.KeyLeftRight)
        self.canvas.focus_set()
        
        self.canvas.bind("<Button-1>", self.MouseEventUp)
        self.canvas.bind('<Button-3>', self.MouseEventDown)
        
        
        window.mainloop()
      
    def KeyLeftRight(self, event):
        if self.inBounds():
            if event.keysym == 'Left':
                self.canvas.delete('circle')
                self.x1 -= 2
                self.x2 -= 2
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags = 'circle')
            elif event.keysym == 'Right':
                self.canvas.delete('circle')
                self.x1 += 2
                self.x2 += 2
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags = 'circle')
        return
    
    def MouseEventUp(self, event):
        if self.inBounds():
            self.canvas.delete('circle')
            self.y1 -= 2
            self.y2 -= 2
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags = 'circle')
        return
    
    def MouseEventDown(self, event):
        if self.inBounds():
            self.canvas.delete('circle')
            self.y1 += 2
            self.y2 += 2
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, tags = 'circle')
        return
    
    def inBounds(self):
        if (self.self.x1 > 0 and self.self.x2 < 300 
                and self.self.y1 < 0 and self.self.y2 < 300):
            return True
        else:
            return False

start = Animation()
