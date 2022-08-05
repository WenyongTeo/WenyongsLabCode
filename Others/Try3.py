#lab2 exq1()
#Write a program that reads in the hours worked for a hourly paid employee.
# The rate is $6 per hour for the first 8 hours and 1.5 times the rate for hours in excess of 8.
# Print the pay after the user enters the hour. E.g.

def pay():
    hourly= float(input("How many hours did you work?: "))
    if hourly <= 8:
        noOvertime= 6*hourly
        print(f'The paid amount is ${noOvertime:.2f}')
    else:
        Overtime= (hourly-8) * (6*1.5) + (8*6)
        print(f'The overtime paid is ${Overtime:.2f}')
#pay()

def result():
    marks= int(input("Whats your marks? "))
    if marks >= 80:
        print("Distinction")
    elif marks >=65 and marks <=79:
        print("Credit")
    elif marks >=50 and marks <= 64:
        print('Pass')
    else:
        print('Fail')
#result()

def pay():
    hourly= float(input("How many hours did you work?: "))
    if hourly <= 8:
        noOvertime= 6*hourly
        print(f'The paid amount is ${noOvertime:.2f}')

    elif hourly <=12 :
        Overtime= (8*6)+ (6*1.5)*(hourly-8)
        print(f'The overtime paid is ${Overtime:.2f}')

    else:
        Overtime= 36 + 48 + (hourly-12)*2
        print(f'The overtime pay after 12 hours is ${Overtime:.2f}')
#pay()

def nric():
    n= input("Nric ")
    if n[1:8].isalpha():
        print("What? theres no 7 digits")
    elif n[0] in ['S','T','F','G']:
        print('Hello please its not true')
    else:
        print('invalid yo')
nric()

