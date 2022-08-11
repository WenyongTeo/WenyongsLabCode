def main():
    diceValue, tries = 4, 1
    while tries <= 3:
        guess = int(input(f"Try {tries}. Enter guess: "))
        if diceValue == guess:
            print("You got it!")
            break
        print("Incorrect")
        tries += 1
    if tries > 3:
        print("Sorry, value is {}".format(diceValue))

    #for-else
    diceValue = 4
    for tries in range(1,4):
        guess = int(input("Try {}. Enter guess: ".format(tries)))
        if diceValue == guess:
            print("You got it!")
            break
        print("Incorrect")
    else: #if loop executed fully then else: <body> will be executed
        print("Sorry, value is {}".format(diceValue))
main()
