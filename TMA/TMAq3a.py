#implement function getHandOfShapes(size, auto)
#size = number of shapes, auto = boolean
#if auto = True random select shapes. Size >=3
#if auto = False function will ask to indicate
#return shape as a list
import random
def getRandomShape():
    theList = ['SCISSOR','PAPER','STONE']
    randomShape = random.choice(theList)
    return randomShape

def getHandOfShapes(size, auto):
    list = []
    i=0
    while not auto:
        while i<size:
            shape = input(f"Shape {i+1} What shape?: ")
            list.append(shape)
            i+=1

        return print(list)
    while auto:
        while i<size:
            list.append(getRandomShape())
            i+=1
        return print(list)


def tma3a():
    auto = input("Auto yes or no: ").lower()
    size = int(input('What size?: '))
    if auto in 'no':
        auto = False
    elif auto in 'yes':
        auto = True
    auto_manual = getHandOfShapes(size, auto)
tma3a()

