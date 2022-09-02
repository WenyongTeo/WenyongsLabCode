# 1st enter name of player
# 2nd each round computer will choose random. round+=1
# 3rd compare your shape vs computer,
# if you win. points+=1 tie no point
# display score before round. score{points}
# 4th 3 round max while rounds<3
# 5th if tie. play another game

import random
def getRandomShape():
    digits = random.randint(1, 3)
    if digits == 1:
        return 'SCISSORS'
    if digits == 2:
        return 'PAPER'
    if digits == 3:
        return 'STONE'


def getShape(rounds, name):
    userShape = input(f'Round {rounds}: {name} Please select a shape: ').upper()
    if userShape not in "SCISSORSPAPERSTONE":
        print('Invalid input')
    return userShape


def main():
    name = input("Enter Players name: ")
    mypoints = 0
    aipoints = 0
    rounds = 1
    while True:
        while rounds < 4:

            my_choice = getShape(rounds, name)
            pc_choice = getRandomShape()
            print(f'Round {rounds} Computer shape is : {pc_choice}')

            if my_choice == pc_choice:
                mypoints += 0
                aipoints += 0
            elif my_choice == 'SCISSORS':
                if pc_choice == 'PAPER':
                    mypoints += 1
                else:
                    aipoints += 1

            elif my_choice == 'PAPER':
                if pc_choice == 'STONE':
                    mypoints += 1
                else:
                    aipoints += 1
            elif my_choice == 'STONE':
                if pc_choice == 'SCISSORS':
                    mypoints += 1
                else:
                    aipoints += 1
            rounds += 1
            print(f'<<{name} {mypoints} : Computer {aipoints}>>')
        if mypoints > aipoints:

            print(f'{name} win!')
            break
        elif aipoints > mypoints:

            print('Computer wins!')
            break
        else:
            print(f'<<{name} {mypoints} Computer {aipoints} Tie, Rematch>>\nNew match')
            rounds=1
            aipoints = 0
            mypoints =0

main()
