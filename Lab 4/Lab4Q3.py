'''
(List) Write a program to record the statistics of 100 throws of a dice.
Use an initial list as follows to record the occurrences of each value of the dice:
diceCount = [0, 0, 0, 0, 0, 0, 0]
The element at index 0 of the list will not be used. When the dice value is 1, add 1 to
index 1 of the list etc. After 100 throws of the dice, display a summary of the
occurrences of the dice values as follows:
Dice Occurrence
1 16
2 14
3 15
4 17
5 18
6 20
Total 100
'''
from random import randint
def rollDice():
     return randint(1,6)

def playGuessingGame():
    for tries in range(1,100+1):
        count = rollDice()
        print(count)
playGuessingGame()
'''
def main():
    diceValue = count
    one = diceValue.count('1')
    two = diceValue.count('2')
    three = diceValue.count('3')
    four = diceValue.count('4')
    five = diceValue.count('5')
    six = diceValue.count('6')
    print("Dice          Occurrence")
    print(f"1            {one}")
    print(f"2            {two}")
    print(f"3            {three}")
    print(f"4            {four}")
    print(f"5            {five}")
    print(f"6            {six}")
    total = 0
    total += rollDice()
    print(f'{total}')
main()
'''


