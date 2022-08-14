'''
for…range) The program starts by asking how many rounds the player wishes to play the game.
When all the rounds are over,display the number of times the player made the correct guess.
How many rounds to play? : 5
Round 1: Head or Tail (H or T): H
Correct!
Round 2: Head or Tail (H or T): T
Wrong!
…
Round 5: Head or Tail (H or T): H
Correct!
You guess 3 correct out 5 rounds.
'''
from random import choice
from lib import getCharSet


def playOneGame(roundNumber):  # was lab3Q6a()
    flipOutcome = choice("HT")
    # print(flipOutcome)
    guess = getCharSet("Round {}: Head or Tail (H or T): ".format(roundNumber), "HTht")

    if guess.upper() == flipOutcome:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def lab3q6b():
    wins = 0
    rounds = int(input("How many rounds to play? : "))
    for i in range(1, rounds + 1):
        wins = wins + playOneGame(i)

    print("You guess {} correct out of {} rounds.".format(wins, rounds))


def lab3q6c():
    noOfTries = 0
    while True:
        noOfTries += 1
        if playOneGame(noOfTries) == 1:
            break

    print("You got it in {} tosses.".format(noOfTries))


def lab3q6d():
    while True:
        lab3q6c()
        playAgain = getCharSet("Play again? (y/n): ", "YyNn")
        if playAgain in "Nn":
            break

    print("Program end")


lab3q6d()