from tkinter import *

def printInput():
    print("Input:", inputBox.get())

def printRadio():
    print("Radio Button:", v.get())

window = Tk()
window.title("Example Window")

frame = Frame(window)
inputBox = Entry(frame)
enter = Button(frame, text='Enter', command=printInput)

v = IntVar()
r1 = Radiobutton(frame, text='This is the first radio button', variable=v, value=1, command=printRadio)
r2 = Radiobutton(frame, text='This is the second radio button', variable=v, value=2, command=printRadio)
r3 = Radiobutton(frame, text='This is the third radio button', variable=v, value=3, command=printRadio)

frame.pack()
inputBox.pack()
enter.pack()
r1.pack()
r2.pack()
r3.pack()

window.mainloop()