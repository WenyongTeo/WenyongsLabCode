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

def Cal():

    ari1, ari2 = float(input('Enter arithmetic expression: ')).split('+,-,+,/')
    add = ari1 + ari2
    minus = ari1 - ari2
    multiply = ari1 * ari2
    division = ari1 / ari2
    if ari1 + ari2:
        print(f'{add}')
    elif ari1 - ari2:
        print(f'{minus}')
    elif ari1 * ari2:
        print(f'{multiply}')
    elif ari1 / ari2:
        print(f'{division}')
    else:
        print('not valid')


Cal()

