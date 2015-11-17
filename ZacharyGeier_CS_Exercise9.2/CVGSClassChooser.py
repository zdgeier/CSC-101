from tkinter import *
from tkinter import ttk

class CVGSClassChooser:
    def __init__(self):
        window = Tk()

        window.title("CVGS Class Chooser")

        frame1 = Frame(window)
        frame1.pack()
        self.label1 = Label(frame1, text="Result")

        L_firstName = Label(frame1, text="First Name: ")
        L_lastName = Label(frame1, text="Last Name: ")
        L_math = Label(frame1, text="Math: ")
        L_science = Label(frame1, text="Science: ")
        L_lab = Label(frame1, text="Senior STEM Lab: ")

        self.first = StringVar()
        self.last = StringVar()
        self.mathVar = StringVar()
        self.scienceVar = StringVar()
        self.labVar = StringVar()
        mathCombo = ['Calculus', 'Linear Algebra', 'Connections']
        scienceCombo = ['Computer Science', 'Anatomy']
        labCombo = ['App Development', '3D Printing', 'Photoshop', 'Robotics']

        self.firstName = Entry(frame1, textvariable=self.first)
        self.lastName = Entry(frame1, textvariable=self.last)
        self.math = ttk.Combobox(frame1, values=mathCombo, textvariable=self.mathVar, state='readonly')
        self.science = ttk.Combobox(frame1, values=scienceCombo, textvariable=self.scienceVar, state='readonly')
        self.lab = ttk.Combobox(frame1, values=labCombo, textvariable=self.labVar, state='readonly')

        self.fn = Label(frame1, textvariable=self.first)
        self.ln = Label(frame1, textvariable=self.last)
        self.m = Label(frame1, textvariable=self.mathVar)
        self.s = Label(frame1, textvariable=self.scienceVar)
        self.l = Label(frame1, textvariable=self.labVar)

        self.confirm = Button(frame1, text='Confirm', command=self.outputResults)

        L_firstName.grid(row=1, column=1, sticky=W)
        L_lastName.grid(row=2, column=1, sticky=W)
        L_math.grid(row=3, column=1, sticky=W)
        L_science.grid(row=4, column=1, sticky=W)
        L_lab.grid(row=5, column=1, sticky=W)

        self.firstName.grid(row=1, column=2)
        self.lastName.grid(row=2, column=2)
        self.math.grid(row=3, column=2)
        self.science.grid(row=4, column=2)
        self.lab.grid(row=5, column=2)
        self.confirm.grid(row=6, column=2, sticky=E, pady=10, padx=10)

        window.mainloop()

    def outputResults(self):
        self.firstName.destroy()
        self.lastName.destroy()
        self.math.destroy()
        self.science.destroy()
        self.lab.destroy()
        self.confirm.destroy()

        self.fn.grid(row=1, column=2)
        self.ln.grid(row=2, column=2)
        self.m.grid(row=3, column=2)
        self.s.grid(row=4, column=2)
        self.l.grid(row=5, column=2)

start = CVGSClassChooser()
