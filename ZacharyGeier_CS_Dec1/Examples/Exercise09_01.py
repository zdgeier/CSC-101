from tkinter import * # Import tkinter

class MainGUI():
	def left(self):
		self.canvas.move("ball", -5, 0)
	
	def right(self):
		self.canvas.move("ball", 5, 0)
	
	def down(self):
		self.canvas.move("ball", 0, 5)
	
	def up(self):
		self.canvas.move("ball", 0, -5)
	
	def __init__(self):
		window = Tk() # Create a window
		window.title("Moving Ball") # Set a title
		
		width = 200
		height = 100
		
		self.canvas = Canvas(window, bg = "white", width = width, height = height)
		self.canvas.pack()
		self.canvas.create_oval(10, 10, 20, 20, fill = "red", tags = "ball")
		
		frame = Frame(window)
		frame.pack()
		
		btLeft = Button(frame, text = "Left", command = self.left).pack(side = LEFT)
		btRight = Button(frame, text = "Right", command = self.right).pack(side = LEFT)
		btUp = Button(frame, text = "Up", command = self.up).pack(side = LEFT)
		btDown = Button(frame, text = "Down", command = self.down).pack(side = LEFT)
		
		window.mainloop() # Create an event loop

MainGUI()
