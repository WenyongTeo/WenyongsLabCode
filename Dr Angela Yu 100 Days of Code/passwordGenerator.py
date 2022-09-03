# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwords = []
password = ''
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for a in range(1, nr_letters + 1):
    randomL = random.choice(letters)
    # numberLetters = len(letters)
    # randomLetters = random.randint(0,numberLetters-1)
    # randomL = letters[randomLetters]
    # random.shuffle(randomL)

    passwords += randomL

for b in range(1, nr_numbers + 1):
    randomL = random.choice(numbers)
    # numberNumbers = len(numbers)
    # randomNumbers = random.randint(0,numberNumbers-1)
    # randomN = numbers[randomNumbers]
    # random.shuffle(randomN)
    passwords += randomL

for c in range(1, nr_symbols + 1):
    randomS = random.choice(symbols)
    # numberSymbols = len(symbols)
    # randomSymbols = random.randint(0,numberSymbols-1)
    # randomS = symbols[randomSymbols]
    # random.shuffle(randomS)
    passwords += randomS
random.shuffle(passwords)

for char in passwords:
    password += char
print(password)

'''randomPass = randomS+randomN+randomL
random.shuffle(randomPass)'''
'''import random
def gen(symbols, length):
    myrg = random.SystemRandom()
    return ''.join(myrg.sample(symbols, length))

symbols = "abcdefghijklmnopqrstuvxyz123567890_#?!"
length = 10
for _ in range(10):
    print(gen(symbols, length))'''