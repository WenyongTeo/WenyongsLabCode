# Second level design
from random import randint


def rollDice():  # roll dice has the value of 1 to 6 and will be random
    return randint(1, 6) #3. this code will return a random number from 1 to 6 to line40 rollDice(). for example 3


# =======================================================================================================================
# Third-Level Design
def getPlayerGuess(tries):  #8. getPlayerGuess(1)
    return int(input("Try {}. Enter guess: ".format(tries))) #9. player will input his guess. lets say 3.
                                                            #getPlayerGuess will be 3 now and will return it to line 28

def checkGuess(guess, diceValue):  # checkGuess #12. from line29. this function will execute. guess is 3 diceValue is 3
    success = diceValue == guess #success = 3 = 3
    if success:
        print("You got it!") #only happen if both dicevalue and guess is same number
    else:
        print("Incorrect")
        return success #13. print "you got it"


# =======================================================================================================================
# Second-Level Design
def playGuessingGame(diceValue): #5. The diceValue here is 3. got from line40
    for tries in range(1, 4): #6 this will loop the value tries 3 times. 1 2 3
        guess = getPlayerGuess(tries) #7. 1st try, go line 11 to get the value of getPlayerGuess. #10. guess = 3 since getPlayerGuess(1) is 3
        if checkGuess(guess, diceValue): #11. This function is at line15, (3,3)
            break
        else:
            print(f"sorry, value is {diceValue}")


# =======================================================================================================================
# Top level design, (the one executing)
def main():
    playAgain = 'y'
    while playAgain[0].lower() in 'yY': #1. if user enter playAgain yY will execute the loop
        diceValue = rollDice() #2. diceValue will be returned from rollDice() line5 for example. 3
        playGuessingGame(diceValue) #4. playGuessingGame(3) will execute the playGuessingGame function at line 26
        playAgain = input("Continue? y/n: ") #15. will ask you wanna play again?
    print("End game")


main()
