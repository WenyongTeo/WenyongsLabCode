def lab3q1a():
    n = int(input("Enter first number here: "))
    x = int(input("Enter second number here: "))
    for i in range(n,x+1):
        print(i,'')

def lab3q1b():
    n = int(input("Enter first number here: "))
    x = int(input("Enter second number here: "))
    sum = 0
    for i in range(n, x + 1):
        sum+=i
    print(f'{sum}')

def lab3q1c():
    n = int(input("Enter first number here: "))
    x = int(input("Enter second number here: "))
    sum=0
'''    ''if n<x:''
'''
#lab3q1c()

def primeChecker(number):
    isPrime=True
    for i in range(2,number):
        if number%i == 0:
            isPrime = False
    if isPrime:
        print("its prime")
    else:
        print("this aint prime")

#number = int(input('What number '))
#primeChecker(number)

'''def doSomething(s):
    n=0
    for c in range(len(s)):
        if int(s[c])%2==0:
            n+1
    return n
'''

def main():
    number = int(input("enter number here:"))
    if number/10==1 or number%10==1:
        print("valid",number)
    else:
        print("invalid")
def main2():
    #same=A
    #first last same =B
    #first last not same =C
    List=[]
    F,M,L = str(input('Enter 3 characters: '))
    if F==M==L:
        print("A")
    elif F==L:
        print("B")
    elif F!=L:
        print("C")

def main3():
    nList = [1,2,3]
    num1= int(nList[0])
    num2= int(nList[1])
    num3= int(nList[2])
    Sum = num1+num2+num3
    if Sum%2==1:
        print('Odd')
    else:
        print("Even")

def main4():
    s=str(input("enter here: "))
    for i in s[::-1]:
        print(int(i)-1)
def main5()
    d = str(input("Enter digits here: "))
    if sum
main5()

