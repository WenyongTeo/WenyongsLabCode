
def divide(x,y):
    quotient = 0
    while x-y >0:
        x = x - y
        quotient +=1
    remainder = x
    return quotient,remainder
#return pass the value back to caller
def main():
    num1 = int(input('Enter 1 '))
    num2 = int(input('Enter 2 '))

    quotient, remainder = divide(num1,num2) #caller
    print(f'{num1} divide {num2} will give quotient {quotient} and remainder {remainder}')
main()