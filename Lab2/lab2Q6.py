#(if…elif…else) Write a program that determines whether two integers are even or odd.
# Display one of the following messages:
#- “The 2 numbers are even”
#- “The 2 numbers are odd”
#- “One number is even and the other is odd”

def main():
    number1= float(input("Enter number 1: "))
    number2= float(input('Enter number 2: '))
    if (number1 % 2) == 0 and (number2 % 2) == 0:
        print("The 2 numbers are even")

    elif (number1 % 2) == 1 and (number2 % 2) == 1:
        print('The 2 numbers are odd')

    else:
        print('One number is even and the other is odd')


main()
