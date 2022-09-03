'''size1 = (0, 0, 0)
size2 = (155, 80, 70)
size3 = (160, 88, 76)
size4 = (165, 96, 84)
size5 = (170, 104, 92)
size6 = (175, 112, 100)
size7 = (180, 120, 108)
size8 = (185, 128, 116)

Nested list
height = input('h')
chest = input('c')
waist = input('w')
heightSize = [0,155,160,165,170,175,180,185,]
chestSize = [0,80,88,96,104,112,120,128,]
waistSize = [0, 70, 76, 84, 92, 100, 108, 116]
chart= [heightSize,chestSize,waistSize]
print(chart[0][0])
'''
'''from random import randint
#aiChoice = ['Rock', 'Paper', 'Scissor']
#threeChoice = len(aiChoice)
def getRandomShape():
    randomChoice = randint(0, 2)
    if randomChoice == 0:
        aiChoice = 'Rock'
    elif randomChoice == 1:
        aiChoice = 'Paper'
    else:
        aiChoice = 'Scissor'
    return aiChoice

def main():
    print(getRandomShape())
main()
'''

score = (11 * (8/7)) + (5 * (8/5))  + 20 + 9


print(score)
