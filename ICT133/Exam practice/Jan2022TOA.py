'''def TOA2022Janq1a():
    s = input("Enter here:")
    if len(s)>8:
        print("invalid must be 8")
    elif not s[0].isupper():
        print("Invaild first letter must be caps")
    elif not s[3:7].isnumeric():
        print('Digit')
    elif s[7] not in ['S','X','Z']:
        print(s[7])
    else:
        print("Valid")
TOA2022Janq1a()'''

'''def TOA2022Janq1b():
    n = int(input('Enter your number '))
    i=0
    while i<n:
        print(n/n)
        i+=1
TOA2022Janq1b()'''
'''def getDurationInMinutes(duration):
    hour=int(duration[0])
    min=int(duration[1])
    duration = (hour*60)+min
    return duration

def computeCharge(mins):
    charge = 0
    if 10<mins<60:
        charge+=1.5
    elif mins>=60:
        charge=((mins/60)+0.2)+(1.5)
    if charge >5:
        charge = 5
    print(charge)

def q2():
    duration = input("Enter hour and min in format h:mm ").split(':')
    mins = getDurationInMinutes(duration)
    computeCharge(mins)
q2()'''

'''def q3():
    qtyPrice = [2,1.5,4,0.5,1,2.5,3,2.0]
    unit = qtyPrice[::2] #::2 = increment 2, take every 2nd number
    price = qtyPrice[1::2]# qtyprice[1] =1.5 increment 2 from 1.5 = 0.5 2.5 2.0
    items = 0
    maxPrice=0
    for i in range(len(unit)):
        print(f"{unit[i]} X {price[i]}= {unit[i]*price[i]}") #will display the unit and then the price
        items+=1
        maxPrice+=unit[i]*price[i]
    print(f'Total items is {items}')
    print(f"Final price is {maxPrice:.2f}")
q3()'''

'''def q3b():
    numList=[]
    list=0
    while list<5:
        num=input('Enter num: ')
        for i in range(len(numList)):
            if num<=numList[i]:
                numList.insert(i,num)
                break
        else:
            numList.append(num)
        print(numList)
        list+=1
q3b()'''

def q4a():
    seatingPlan = {'A': ['O', 'X', 'O', 'X'], 'B': ['O', 'O', 'O', 'X'], 'C': ['O', 'X', 'O', 'O']}
    with open('../seatingPlan.txt', 'w') as f:
        f.write(Plan)
q4a()
