


'''from random import randint,choice
def getPlayers():
    players = []
    for i in range(3)
        name = input('Name')
        players.append[name,0]
    return [['A',3]],['B',4],['C',4]
def playGuessingGame(players,diceValue):
    seq= choice[[0,1],[1,2,0],[2,1,0]]
    print('seq is', seq)
    while True:
        for i in seq:
            guess

def printGameSummary(players):
    maxScore = max[p[1] for p in player])
        for p in player:
            if p[1] in players:
                if p[1] == maxScore:
                    print(p[0], end='')
def main():
    players = getPlayers()
    while True:
        diceValue=rollDice
        print(diceValue)
        playGuessingGame(players,diceValue)
        playAgain = input('Enter y or n')
        if playAgain[0].lower == 'n'
            break
    print


'''

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
import math
import random

'''def playOffs(name):
    aipoints = 0
    mypoints = 0
    game = 1
    shapes = ['SCISSORS', 'STONE', 'PAPER']
    while aipoints == mypoints:
        while True:
            my_shape = input(f'Play off {game} Enter your shape: ').upper()
            if my_shape not in shapes:
                print("Invalid Shape!")
            else:
                break
        ai_shape = random.choice(shapes)
        print(f'Playoff {game} Computer shape is : {ai_shape}')
        if my_shape == ai_shape:
            mypoints += 0
            aipoints += 0
        elif my_shape == 'SCISSORS':
            if ai_shape == 'PAPER':
                mypoints += 1
            else:
                aipoints += 1

        elif my_shape == 'PAPER':
            if ai_shape == 'STONE':
                mypoints += 1
            else:
                aipoints += 1
        elif my_shape == 'STONE':
            if ai_shape == 'SCISSORS':
                mypoints += 1
            else:
                aipoints += 1
        print(f'Rounds {game} {name} {my_shape} : Computer {ai_shape}')
        game+=1
        if mypoints>aipoints:
            return print(f'\n{name} wins the playoff!!')
        elif aipoints>mypoints:
            return print(f'\nComputer wins the playoff!!')


def main():
    name= 'wy'
    playOffs(name)

main()'''
a1 = True
b2 = False

if a1 and b2:
    print(a1 and b2)
elif a1:
    print(a1)
