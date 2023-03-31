'''a,b = 16,5
c= 0
while True:
    if a>=b:
        c=c+1
        a=a-b
    else:
        break
print(a,b,c)'''

'''s = 'abcdefgh'
newS= ''
for i in range(0,len(s),3): #0-7, increment by 3
    newS += s[i].upper() + s[i+1:i+3] #i=0 +1= s[1] = b, 0+3 = 3. s[3] = c
    print(newS)'''

def larger(a,b):
    return a if a > b else b

def largest(aList):
    theLargest = aList[0]
    for i in range(1,len(aList)):
        if theLargest<aList[i]:
            theLargest=aList[i]
    return theLargest

students = {'John':53,'Ann':62,'Peter':45,'Tom':62}

