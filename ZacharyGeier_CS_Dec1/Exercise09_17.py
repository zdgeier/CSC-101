from tkinter import *

class Car:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.draw(x,y)

    def draw(self, x, y):
        self.canvas.delete('all')
        self.canvas.create_rectangle(x, y-20, x+50, y-10, fill='grey')
        self.canvas.create_oval(x+10, y, x+20, y-10, fill='black')
        self.canvas.create_oval(x+30, y, x+40, y-10, fill='black')
        self.canvas.create_polygon(x+10,y-20,x+20,y-30,x+30,y-30,x+40,y-20, fill='black')

class RacingCar:
    def __init__(self):
        window = Tk()
        
        self.w = 300
        self.h = 300

        self.canvas = Canvas(window, width=self.w, height=self.h)
        self.canvas.pack()

        self.car = Car(self.canvas, 0, self.h)
        self.speed = 4

        self.canvas.bind("<Key>", self.keyPressRight)
        self.canvas.focus_set()
        self.animate()
        
        window.mainloop()

    def animate(self):
        while True:
            self.canvas.after(30) # Sleep
            self.canvas.update() # Update self.canvas

            if self.car.x < self.w:
                self.car.x += self.speed
                self.car.draw(self.car.x, self.car.y)
            else:
                self.car = Car(self.canvas, -50, self.h)
        
    def keyPressRight(self, event):
        if event.keysym == 'Up':
            self.speed += 3
        elif event.keysym == 'Down' and self.speed <= 3:
            self.speed = 0
        elif event.keysym == 'Down':
            self.speed -= 3

start = RacingCar()