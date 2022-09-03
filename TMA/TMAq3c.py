#hand has n shapes. cannot have n/2.floor of same shape
#compare if tie go play off 4/2= 2 so paper can only have 2 if size = 2
#in play off. will be similar to 2a where each player
# choose 1 until winner is decided
import math
import random
def playOffs(name):
    aipoints = 0
    mypoints = 0
    game = 1
    shapes = ['SCISSORS', 'STONE', 'PAPER']
    while aipoints == mypoints:
        while True:
            my_shape = input(f'Playoff {game} Enter your shape: ').upper()
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
        print(f'Playoff {game}: {name} chose {my_shape} : Computer chose {ai_shape}')
        game+=1
        if mypoints>aipoints:
            return print(f'\n{name} wins the playoff!!')
        elif aipoints>mypoints:
            return print(f'\nComputer wins the playoff!!')
#ai condition
def getRandomShape(size):
    aiList = []
    onelist = ['SCISSORS', 'PAPER', 'STONE']
    maxShape = math.floor(size / 2)
    while len(aiList)<size:
        randomShape = random.choice(onelist)
        shapeCountAi = aiList.count(randomShape)
        if shapeCountAi == maxShape:
            aiList.remove(randomShape)
        else:
            aiList.append(randomShape)
    return aiList

def getHandOfShapes(size, auto):
    playerlist = []
    onelist = ['SCISSORS', 'PAPER', 'STONE']
    maxShape = math.floor(size / 2)
    while not auto:
        while len(playerlist) < size:
            shapes = input("enter shapes (SCISSORS', 'PAPER', 'STONE): ").upper()
            if playerlist.count(shapes) == maxShape:
                print(f'Cannot have more than {maxShape} {shapes}')
            else:
                playerlist.append(shapes)
        return playerlist

    while auto:
        while len(playerlist) <size:
            randomShape = random.choice(onelist)
            shapeCountPlayer = playerlist.count(randomShape)
            if shapeCountPlayer == maxShape:
                playerlist.remove(randomShape)
            else:
                playerlist.append(randomShape)
        return playerlist

def tma3c():
    mypoints = 0
    aipoints = 0
    game = 1
    auto = input("Auto or no? (Yes or No): ").lower()
    if auto in 'no':
        auto = False
    elif auto in 'yes':
        auto = True
    size = int(input('What size?(Must be more than 3: '))

    if size < 3:
        print('Invalid, size is less than 3: ')
    else:
        name = input('What is your name: ')
        my_choice = getHandOfShapes(size, auto)
        print('\nGame starts...')
        for i in range(size):
            ai_choice = getRandomShape(size)
            print('')
            print(f'Rounds {game}: {name} {my_choice[i]} : Computer {ai_choice[i]}')
            if my_choice[i] == ai_choice[i]:
                mypoints += 0
                aipoints += 0
            elif my_choice[i] == 'SCISSORS':
                if ai_choice[i] == 'PAPER':
                    mypoints += 1
                else:
                    aipoints += 1

            elif my_choice[i] == 'PAPER':
                if ai_choice[i] == 'STONE':
                    mypoints += 1
                else:
                    aipoints += 1

            elif my_choice[i] == 'STONE':
                if ai_choice[i] == 'SCISSORS':
                    mypoints += 1
                else:
                    aipoints += 1
            i += 1
            game += 1
            print(f'<<{name} {mypoints} : Computer {aipoints}>>')  # << Alan 1 : Computer 0 >>

        if aipoints == mypoints:
            print('\nTie! time to rematch!\n')
            playOffs(name)
        elif aipoints > mypoints:
            print('Computer win!')
        elif mypoints > aipoints:
            print(f'{name} win!')

tma3c()

