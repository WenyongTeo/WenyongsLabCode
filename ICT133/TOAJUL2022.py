#coin fair if prob of heads is 0.45 and 0.55
#n1 heads, n2 tails
#def q1i():

#
#if letter "A" appears same number of time in both 1/2s of string print same
#more if "A" appears more in first half
#less if "A" appears less in first halves
#if
'''def q1ii():
    s = str(input("Enter words here: "))
    firstHalf= len(s)//2
    secondHalf= (len(s)//2)+1

q1ii()'''

def q1bi():
    List=[]
    s1 = str(input("Enter words here: "))
    for i in s1:
        List.append(i)
    removeDup = []
    [removeDup.append(x) for x in List if x not in removeDup]
    s2 = ''.join(removeDup)
    print(s2)



def q1bii():
    w1 = str(input("Enter words 1 here: "))
    w2 = str(input("Enter words 2 here: "))
    list1 = []
    list2 = []
    for i in w1:
        list1.append(i)
        list1.sort()
    word1 = ''.join(list1)

    for x in w2:
        list2.append(x)
        list2.sort()
    word2 = ''.join(list2)
    print(word1,word2)
    if word1 == word2:
        print("Possible")
    if word1 != word2:
        print("not possible")
'''Result'''
'''Enter words 1 here: car
Enter words 2 here: mod
acr dmo
not possible
'''
#q1c:

def q2a():

q2a()

#def q4():
