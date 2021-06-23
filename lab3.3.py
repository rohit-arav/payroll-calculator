# Lab 3, Question 3
# Printing a payroll statement

# Inputs
name = input("Enter employee name: ")
hours = float(eval(input("Enter number of hours worked in a week: ")))
pay_rate = eval(input("Enter hourly pay rate: "))
fed_tax = eval(input("Enter federal tax withholding rate: "))
state_tax = eval(input("Enter state tax withholding rate: "))

# Calculations
gross_pay = hours * pay_rate
fed = gross_pay * fed_tax
state = gross_pay * state_tax
total_deduction = fed + state
net_pay = gross_pay - fed - state

# Printing the statements
print("\n")
print("Employee Name: " + name)
print("Hours Worked: " + format(hours, "<.1f"))
print("Pay Rate: " + "$" + format(pay_rate, "<.2f"))
print("Gross Pay: " + "$" + format(gross_pay, "<.2f"))
print("Deductions: ")
print("   Federal Withholding " + "(" + format((fed_tax*100), "<.1f") + "%): " + "$" + format(fed, "<.2f"))
print("   State Withholding " + "(" + format((state_tax*100), "<.1f") + "%): " + "$" + format(state, "<.2f"))
print("Net Pay: " + "$" + format(net_pay, "<.2f"))







