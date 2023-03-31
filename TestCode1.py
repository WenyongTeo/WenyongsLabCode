#This is for testing codes. 
'''haram = ['pig','smoke','piakpiakbeforemarriage']
isithalal= input('Is that halal?: ')
halalChecker = True
while halalChecker:
   if isithalal in haram:
    halalChecker = False
    print('EH TAK HALAL LA SIAL')
   else:
    halalChecker = True
    print('That is halal')'''
def q1():
    n1= int(input("Enter number 1: "))
    n2= int(input("Enter number 2: "))
    for i in range(n1,n2+1):
        print(i)
def q1b():
    n1= int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    n3=0
    for i in range(n1,n2+1):
        print(i)
        n3+=i
    print(n3)

def q1c():
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    sum=0
    if n1<=n2:
        step = 1
    else:
        step = -1
    for i in range(n1,n2+step,step):
        sum+=i
        print(i)
    print(sum)
q1c()
