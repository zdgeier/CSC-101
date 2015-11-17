from tkinter import *

class InvestmentCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment Calculator")

        frame1 = Frame(window)
        frame1.pack()
        self.label1 = Label(frame1, text="Result")

        frame2 = Frame(window)
        frame2.pack()

        L_result = Label(frame2, text="Result: ")
        L_investmentAmount = Label(frame2, text="Enter investment amount: ")
        L_monthlyInterest = Label(frame2, text="Enter monthly interest: ")
        L_years = Label(frame2, text="Enter years: ")

        self.investment = DoubleVar()
        self.interest = DoubleVar()
        self.yrs = DoubleVar()
        self.futureValue = StringVar()

        result = Label(frame2, textvariable=self.futureValue)
        investmentAmount = Entry(frame2, textvariable=self.investment)
        monthlyInterest = Entry(frame2, textvariable=self.interest)
        years = Entry(frame2, textvariable=self.yrs)

        confirm = Button(frame2, text="Calculate", command=self.calculate)

        L_investmentAmount.grid(row=1, column=1, sticky=W)
        L_monthlyInterest.grid(row=2,column=1, stick=W)
        L_years.grid(row=3,column=1, sticky=W)
        L_result.grid(row=4, column=1, sticky=E)

        investmentAmount.grid(row=1, column=2)
        monthlyInterest.grid(row=2,column=2)
        years.grid(row=3,column=2)
        result.grid(row=4,column=2)
        confirm.grid(row=5,column=2)

        window.mainloop()

    def calculate(self):
        self.futureValue.set(
            format(self.investment.get() * (1 + (self.interest.get()/12) * .01) ** (self.yrs.get() * 12), '2.2f')
        )

inv = InvestmentCalculator()