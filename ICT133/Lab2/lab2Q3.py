#(if…else) Write a program that reads in 2 integer values. Display one of the following messages:
#- “The 2 numbers are the same”
#- “The 2 numbers are not the same”

def main():
    number1 = int(input('Enter number 1: '))
    number2 = int(input('Enter number 2: '))
    if number1 - number2 == 0:
        print('The 2 numbers are the same')

    else:
        print('The 2 numbers are not the same')


main()