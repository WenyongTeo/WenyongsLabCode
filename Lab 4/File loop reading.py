'''
def main():
    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthName = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    maxDays = max(month) #31 is the max (month) is the function
    for index in range(12): #index = Jan to dec now
        if month[index] == maxDays: #month(jan to dec) = 31
            print(monthName[index]) #print the months with 31 days

    for index in range(12):
        print("Month {} has {} days.".format(index + 1, month[index]))
main()

def getNumbers():
    nums = []
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        nums.append(float(xStr))
        xStr = input("Enter a number (<Enter> to quit) >> ")
        return nums
getNumbers()

def double(value):
    value = 2 * value
    z = value
    return z
def main():
    x = 10
    y = double(x)
    #double is from the first function
    #double(value)
    #value inside the () has the formula of 2*value
    #put value inside z
    #return z means it will return value's calculation of 2*value
    # double(x) means double will initiate the formula of whatever is inside
    #its parameter, so this is x = 2*x
    # z=x
    #return x
    print(x, y)
    #10 , y= 20

    Passing Mutable Values
def double(x):
    x = x.append(2)
    # x= x.append(2) means it will change the value to 2
    z = x
    return z
def main():
    x = [10]
    y = double(x)
    #double is calling the fucntion #double(x)
    #double(x) will change the value of x which is 10 to 2
    #so double(x) makes y = 2
    print(x, y)
    #output is [10,2]
#----------------------------------------------------------------------------------------------------------------------
#Second level design
from random import randint
def rollDice(): #roll dice has the value of 1 to 6 and will be random
    return randint(1,6)
#=======================================================================================================================
#Third-Level Design
def getPlayerGuess(tries): #getPlayerGuess(tries) tries = 
    return int(input("Try {}. Enter guess: ".format(tries)))

def checkGuess(guess, diceValue): #checkGuess
    success = diceValue == guess
    if success:
        print("You got it!")
    else:
        print("Incorrect")
        return success
#=======================================================================================================================
#Second-Level Design
def playGuessingGame(diceValue):
    for tries in range (1,4):
        guess = getPlayerGuess(tries)
    if checkGuess(guess,diceValue):
        break
else:
    print(f"sorry, value is {diceValue}')

#=======================================================================================================================
#Top level design, (the one executing)
def main():
    playAgain = 'y'
    while playAgain[0].lower() in 'yY':
        diceValue = rollDice()
        playGuessingGame(diceValue)
        playAgain = input("Continue? y/n: ")
    print("End game")
main()





'''