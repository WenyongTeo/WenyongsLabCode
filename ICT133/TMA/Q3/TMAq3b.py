# tma3b
# Start game choose hand size
# If size < 3 re-enter
# Ask for players name
# then getHandOfShape
# will Also do computer shapes
# Compare them, if win +=1 points. Tie no points
# If round tie reset game
import random

#
def getRandomShape():
    theList = ['SCISSORS', 'PAPER', 'STONE']
    randomShape = random.choice(theList)
    return randomShape


def getHandOfShapes(size, auto):
    list = []
    i = 0
    while not auto:
        while i < size:
            shape = input(f"Shape {i + 1} What shape?: ").upper()
            list.append(shape)
            i += 1

        return list
    while auto:
        while i < size:
            list.append(getRandomShape())
            i += 1
        return list


def tma3b():
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
            ai_choice = getHandOfShapes(size, True)
            print('')
            print(f'Rounds {game} {name} {my_choice[i]} : Computer {ai_choice[i]}')
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
            input('Tie, re-match!\nPress enter to play again')
            tma3b()
        elif aipoints > mypoints:
            print('Ai win!')
        elif mypoints > aipoints:
            print('You win!')

tma3b()
