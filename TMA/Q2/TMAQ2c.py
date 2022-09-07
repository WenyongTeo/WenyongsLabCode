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
    match = 1

    while mypoints!=3 and aipoints !=3:

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
        rounds+=1
        print(f'<<{name} {mypoints} : Computer {aipoints}>>')
    if mypoints == 3:
        print(f'{name} is the  winner after {rounds} rounds!')
    else:
        print(f'Computer is the winner after {rounds} rounds!')

main()
