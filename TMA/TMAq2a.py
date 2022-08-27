import random
def getRandomShape():
    threeShape = random.randint(1, 4)
    if threeShape == 1:
        threeShape = 'Scissors'
    elif threeShape == 2:
        threeShape = 'Paper'
    elif threeShape == 3:
        threeShape = 'Stone'
    print(threeShape)
    return threeShape

def getShape():
    while True:
        play = input('Play? (Y/N): ')
        if play in 'Yy':
            userShape = input('Please select a Shape: ')
            if userShape.upper() in 'SCISSOR':
                print('Scissors')
            elif userShape.upper() in 'PAPER':
                print('Papers')
            elif userShape.upper() in 'STONE':
                print('Stones')
            else:
                print("Sorry, Please choose between Scissor, Paper, and Stone")
            ()
        else:
            break


def main():
    getShape()

main()