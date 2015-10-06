name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
fedTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

total = hours * rate
fed = total * fedTax
state = total * stateTax

print("\nEmployee Name:", name)
print("Hours Worked:", format(hours, "<2.1f"))
print("Pay Rate: $", format(rate, "<2.2f"), sep='')
print("Gross Pay: $", format(total, "<2.2f"), sep='')
print("Deductions:")

print("  Federal Withholding (" + str(fedTax * 100) + "%): $",
      format(fed, "3.2f"), sep='')

print("  State Withholding (" + str(stateTax * 100) + "%): $",
      format(state, "3.2f"), sep='')

print("  Total Deduction: $", format(fed + state, "3.2f"), sep='')
print("Net Pay: $", format(total - fed - state, "3.2f"), sep='')


