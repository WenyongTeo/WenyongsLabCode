from random import randint
def main():

    playAgain= 'y'
    while playAgain[0].lower() == 'y':
        diceValue, tries = randint(1, 6), 1
        while tries <= 3:

            tries += 1
        if tries > 3:
            print("Sorry, value is {}".format(diceValue))
        playAgain = input("continue? y/n: ")
    print('End game')
main()