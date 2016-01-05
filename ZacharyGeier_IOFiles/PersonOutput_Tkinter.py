from Person import Person
from tkinter import *

class PersonOutput:
    def __init__(self):
        self.filepath = "PersonOutput.txt"

        window = Tk()
        frame = Frame(window)
        frame.pack()

        self.first = StringVar()
        self.last = StringVar()
        self.color = StringVar()

        L_first = Label(frame, text="First: ")
        L_last = Label(frame, text="Last: ")
        L_color = Label(frame, text="Favorite Color: ")

        E_first = Entry(frame, textvariable=self.first)
        E_last = Entry(frame, textvariable=self.last)
        E_color = Entry(frame, textvariable=self.color)

        B_enter = Button(frame, text='Enter', command=self.enter)

        L_first.grid(row=0, column=0)
        L_last.grid(row=1, column=0)
        L_color.grid(row=2, column=0)

        E_first.grid(row=0, column=1)
        E_last.grid(row=1, column=1)
        E_color.grid(row=2, column=1)

        B_enter.grid(row=3, column=1, padx=10, pady=10)

        window.mainloop()

    def enter(self):
        self.appendData(str(self.first.get()) + "," + str(self.last.get()) + "," + str(self.color.get()))
        self.outputData()

    # Appends data string to file in filepath
    def appendData(self, data):
        file = open(self.filepath, 'a')
        file.write(data + '\n')
        file.close()

    # Outputs people in filepath
    def outputData(self):
        file_r = open(self.filepath, 'r')
        lines = file_r.readlines()
        file_r.close()

        people = []
        for line in lines:
            person_data = line
            person_data = person_data.strip()
            datalist = person_data.split(',')
            people.append(Person(datalist[0], datalist[1], datalist[2]))

        for person in people:
            print(person)

start = PersonOutput()