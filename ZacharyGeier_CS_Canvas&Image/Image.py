from tkinter import *
from PIL import Image, ImageTk

class PictureViewer:
    def __init__(self):
        window = Tk()

        window.title("Image Viewer")

        frame1 = Frame(window)
        frame1.pack()

        self.prompt = Label(frame1, text='Press to see picture of a cat: ')
        self.button = Button(frame1, text='Enter', command=self.showPicture)
        self.image = Image.open('pointers.png')
        self.photo = ImageTk.PhotoImage(self.image)
        self.L_photo = Label(frame1, image=self.photo)

        self.prompt.grid(row=0,column=0, padx=10, pady=10)
        self.button.grid(row=0,column=1, padx=10, pady=10)

        window.mainloop()

    def showPicture(self):
        self.prompt.destroy()
        self.button.destroy()
        self.L_photo.grid()

start = PictureViewer()
