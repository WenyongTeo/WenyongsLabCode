from random import randint


def computerChoice():
    aiChoice = ['Rock', 'Paper', 'Scissor']
    threeChoice = len(aiChoice)
    randomChoice = randint(0, threeChoice - 1)
    selectedChoice = aiChoice[randomChoice]
    return selectedChoice


def myChoice():
    userChoice = input('Enter your choice, (Scissor, Paper, Stone): ')
    return userChoice


def theBattle():
    mine = myChoice()
    his = computerChoice()

    if mine == his:
        print(f"Both chose {mine} TIE!")

    elif mine.upper() == 'PAPER':
        if his.upper() == 'STONE':
            print("Paper win Stone, You Win!")
        else:
            print('Scissor wins Paper, You lose!')

    elif mine.upper() == 'STONE':
        if his.upper() == 'SCISSOR':
            print("Stone wins Scissor, You Win!")
        else:
            print('Paper wins Stone, You lose!')

    elif mine.upper() == 'SCISSOR':
        if his.upper() == 'PAPER':
            print("Scissor wins Paper, You Win!")
        else:
            print('Stone wins Scissor, You lose!')


def main():
    while True:
        play = input("Play? (Y/N): ")
        if play.upper() in 'Y':
            theBattle()
        else:
            print('End of game')
            break


main()