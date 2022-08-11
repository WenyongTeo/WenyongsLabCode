#Write a simple calculator program that performs arithmetic operation on 2 numbers.
#Input consists of 3 values, separated by an arithmetic operator, in the following format:
#float operator float
#where float is any decimal number and operator is either +, -, *, /.
#Run 1
#Enter arithmetic expression: 23.6 + 33.2
#Result: 56.8
#SINGAPORE UNIVERSITY OF SOCIAL SCIENCES (SUSS) ICT133 Lab – Page 3 of 3
#Run 2
#Enter arithmetic expression: 85 % 15
#Invalid arithmetic operation


def cal():
    expression = input("Enter arithmetic expression: ")
    num1, operator, num2 = expression.split()  # default is separator is space
    num1, num2 = float(num1), float(num2)

    if len(operator) != 1 or operator not in "+-*/":
        print("Invalid arithmetic operator")
    elif operator == "+":
        print("Result: {}".format(num1+num2) )
    elif operator == "-":
        print("Result: {}".format(num1-num2) )
    elif operator == "*":
        print("Result: {}".format(num1*num2) )
    else:
        print("Result: {}".format(num1/num2) )


cal()

