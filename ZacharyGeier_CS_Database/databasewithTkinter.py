from tkinter import *

class database:

    def __init__(self, first, last, prefix):
        self.__first = first
        self.__last = last
        self.__prefix = prefix
        return

    def getfirst(self):
        return self.__first

    def getlast(self):
        return self.__last

    def getprefix(self):
        return self.__prefix

    def setfirst(self, fn):
        self.__first = fn
        return

    def setlast(self, ln):
        self.__last = ln
        return

    def setprefix(self, pre):
        self.__prefix = pre
        return
    
class DatabaseViewer:
    def __init__(self):
        self.db = [database('Russell', 'Westbrook', 'Mr.'), database('Kevin', 'Durant', 'Mr.'),
              database('Julius', 'Irvin', 'Dr.')]

        self.current = 0

        self.window = Tk()
        self.frame1 = Frame(self.window)
        self.frame1.pack()

        self.createMainElements()

        self.window.mainloop()

    def createMainElements(self):
        self.window.geometry('150x150')

        self.prefixheading = Label(self.frame1, text = 'Honorific')
        self.prefixlabel = Label(self.frame1, text = self.db[self.current].getprefix())
        self.firstheading = Label(self.frame1, text = 'First Name')
        self.firstlabel = Label(self.frame1, text = self.db[self.current].getfirst())
        self.lastheading = Label(self.frame1, text = 'Last Name')
        self.lastlabel = Label(self.frame1, text = self.db[self.current].getlast())

        self.nextbutton = Button(self.frame1, text='Next', command = self.nextperson)
        self.lastbutton = Button(self.frame1, text='Last', command = self.lastperson)
        self.addbutton = Button(self.frame1, text='Add', command = self.addperson)

        self.prefixheading.grid(row=1, column=1)
        self.prefixlabel.grid(row=1, column=2)
        self.firstheading.grid(row=2, column=1)
        self.firstlabel.grid(row=2, column=2)
        self.lastheading.grid(row=3, column=1)
        self.lastlabel.grid(row=3, column=2)

        self.nextbutton.grid(row=4, column=1)
        self.lastbutton.grid(row=4, column=2)
        self.addbutton.grid(row=5,column=2)

    def nextperson(self):
        if self.current < len(self.db)-1:
            self.current += 1
            self.prefixlabel['text'] = self.db[self.current].getprefix()
            self.firstlabel['text'] = self.db[self.current].getfirst()
            self.lastlabel['text'] = self.db[self.current].getlast()
        return

    def lastperson(self):
        if self.current > 0:
            self.current -= 1
            self.prefixlabel['text'] = self.db[self.current].getprefix()
            self.firstlabel['text'] = self.db[self.current].getfirst()
            self.lastlabel['text'] = self.db[self.current].getlast()
        return

    def addperson(self):
        self.prefixlabel.destroy()
        self.firstlabel.destroy()
        self.lastlabel.destroy()
        self.nextbutton.destroy()
        self.lastbutton.destroy()
        self.addbutton.destroy()

        self.first = StringVar()
        self.last = StringVar()
        self.prefix = IntVar()

        self.mr = Radiobutton(self.frame1, text='Mr.', value=1, variable=self.prefix)
        self.mrs = Radiobutton(self.frame1, text='Mrs.', value=2, variable=self.prefix)
        self.miss = Radiobutton(self.frame1, text='Miss', value=3, variable=self.prefix)
        self.dr = Radiobutton(self.frame1, text='Dr.', value=4, variable=self.prefix)
        self.firstName = Entry(self.frame1, textvariable=self.first)
        self.lastName = Entry(self.frame1, textvariable=self.last)
        self.confirm = Button(self.frame1, text='Confirm', command=self.addToDatabase)

        self.mr.grid(row=1, column=2)
        self.mrs.grid(row=1, column=3)
        self.miss.grid(row=1, column=4)
        self.dr.grid(row=1, column=5)
        self.firstName.grid(row=2, column=2)
        self.lastName.grid(row=3, column=2)
        self.confirm.grid(row=4, column=1)

        self.window.geometry('500x150')

    def addToDatabase(self):
        pref = ''
        if self.prefix.get() == 1: pref = 'Mr'
        elif self.prefix.get() == 2: pref = 'Mrs'
        elif self.prefix.get() == 3: pref = 'Miss'
        elif self.prefix.get() == 4: pref = 'Dr'

        self.db.append(database(self.first.get(), self.last.get(), pref))

        self.mr.destroy()
        self.mrs.destroy()
        self.miss.destroy()
        self.dr.destroy()
        self.firstName.destroy()
        self.lastName.destroy()
        self.confirm.destroy()

        self.createMainElements()

start = DatabaseViewer()