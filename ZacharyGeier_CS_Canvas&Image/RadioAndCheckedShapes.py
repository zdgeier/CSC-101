from tkinter import *

class ShapeViewer:
    def __init__(self):
        window = Tk()

        window.title("Shape Viewer")

        frame1 = Frame(window)
        self.canvas = Canvas(window, width=300, height=150)
        self.canvas.pack()
        frame1.pack()
        self.filled = IntVar()
        self.shape = IntVar()

        R_rect = Radiobutton(frame1, text='Rectangle', value=1, variable=self.shape, command=self.showShape)
        R_oval = Radiobutton(frame1, text='Oval', value=2, variable=self.shape, command=self.showShape)
        C_filled = Checkbutton(frame1, text='Filled', variable=self.filled, command=self.showShape)

        R_rect.grid(row=2,column=1)
        R_oval.grid(row=2,column=2)
        C_filled.grid(row=2,column=3)

        window.mainloop()

    def showShape(self):
        if self.filled.get() == 0:
            self.canvas.delete('all')
            if self.shape.get() == 1:
                self.canvas.create_rectangle(290,10,10,140)
            elif self.shape.get() == 2:
                self.canvas.create_oval(290,10,10,140)
        elif self.filled.get() == 1:
            self.canvas.delete('all')
            if self.shape.get() == 1:
                self.canvas.create_rectangle(290,10,10,140,fill='Black')
            elif self.shape.get() == 2:
                self.canvas.create_oval(290,10,10,140,fill='Black')

start = ShapeViewer()
