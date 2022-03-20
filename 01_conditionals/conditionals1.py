# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 

hrs = input("Enter Hours:")

try:
    h = float(hrs)
except:
    print('Hours must be a valid number.')
    quit()

rate = input("Enter rate:")

try:
    r = float(rate)
except:
    print('Rate must be in a valid number format.')
    quit()

if h > 40:
    regpay = 40 * r
    ot = (h - 40) * (r * 1.5)
    pay = regpay + ot
else:
    pay = h * r

str_pay = "{:.2f}".format(pay)

print('Pay must be $' + str_pay)