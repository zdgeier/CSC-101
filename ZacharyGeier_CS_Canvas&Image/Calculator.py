from tkinter import *

class Calculator:
    def __init__(self):
        window = Tk()
        window.title("Calculator")
        frame1 = Frame(window)
        frame3 = Frame(window)

        button1 = Button(frame1, text='1', command=self.b1)
        button2 = Button(frame1, text='2', command=self.b2)
        button3 = Button(frame1, text='3', command=self.b3)
        button4 = Button(frame1, text='4', command=self.b4)
        button5 = Button(frame1, text='5', command=self.b5)
        button6 = Button(frame1, text='6', command=self.b6)
        button7 = Button(frame1, text='7', command=self.b7)
        button8 = Button(frame1, text='8', command=self.b8)
        button9 = Button(frame1, text='9', command=self.b9)
        button0 = Button(frame1, text='0', command=self.b0)

        buttonequ = Button(frame3, text='Equ', command=self.equ)
        buttonclr = Button(frame3, text='Clr', command=self.clr)

        buttona = Button(frame1, text='+', command=self.add)
        buttons = Button(frame1, text='-', command=self.sub)
        buttonm = Button(frame1, text='*', command=self.mul)
        buttond = Button(frame1, text='/', command=self.div)

        self.output = StringVar()
        self.output.set(' ')

        frame2 = Frame(window)

        E_output = Entry(frame2, textvariable=self.output)

        frame2.pack()
        frame1.pack()
        frame3.pack()

        E_output.grid(row=1,column=0, padx=2, pady=2)
        button1.grid(row=2,column=1, padx=2, pady=2)
        button2.grid(row=2,column=2, padx=2, pady=2)
        button3.grid(row=2,column=3, padx=2, pady=2)
        button4.grid(row=3,column=1, padx=2, pady=2)
        button5.grid(row=3,column=2, padx=2, pady=2)
        button6.grid(row=3,column=3, padx=2, pady=2)
        button7.grid(row=4,column=1, padx=2, pady=2)
        button8.grid(row=4,column=2, padx=2, pady=2)
        button9.grid(row=4,column=3, padx=2, pady=2)
        button0.grid(row=5,column=2, padx=2, pady=2)

        buttona.grid(row=2, column=4, padx=2, pady=2)
        buttons.grid(row=3, column=4, padx=2, pady=2)
        buttonm.grid(row=4, column=4, padx=2, pady=2)
        buttond.grid(row=5, column=4, padx=2, pady=2)

        buttonclr.grid(row=6, column=2, padx=2, pady=2)
        buttonequ.grid(row=6, column=3, padx=2, pady=2)

        window.mainloop()

    def clr(self):
        self.output.set(" ")

    def add(self):
        self.output.set(self.output.get() + '+')

    def sub(self):
        self.output.set(self.output.get() + '-')

    def div(self):
        self.output.set(self.output.get() + '/')

    def mul(self):
        self.output.set(self.output.get() + '*')

    def equ(self):
        self.output.set(eval(self.output.get()))

    def b1(self):
        self.output.set(self.output.get() + '1')
    def b2(self):
        self.output.set(self.output.get() + '2')
    def b3(self):
        self.output.set(self.output.get() + '3')
    def b4(self):
        self.output.set(self.output.get() + '4')
    def b5(self):
        self.output.set(self.output.get() + '5')
    def b6(self):
        self.output.set(self.output.get() + '6')
    def b7(self):
        self.output.set(self.output.get() + '7')
    def b8(self):
        self.output.set(self.output.get() + '8')
    def b9(self):
        self.output.set(self.output.get() + '9')
    def b0(self):
        self.output.set(self.output.get() + '0')

start = Calculator()