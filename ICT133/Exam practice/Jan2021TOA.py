'''submit'''


## 1a (i)
def q1ai(num):
    if num // 10 == 1 or num % 10 == 1:
        print(num, 'Valid')


'''submit'''

# TEST
# q1ai(10)
# q1ai(11)
# q1ai(31)
# q1ai(33)
# q1ai(34)
# q1ai(35)

## 1a (ii)
'''submit'''


def q1aii(threechars):
    first, middle, last = threechars[0], threechars[1], threechars[2]
    if first == middle and middle == last:
        print('Group A')
    elif first == last and first != middle:
        print('Group B')
    else:
        print('Group C')


'''submit'''

## TEST
# q1aii('222')
# q1aii('232')
# q1aii('223')
# q1aii('213')

## 1a (iii)
'''submit'''


def q1aiii(nList):
    if sum(nList[1::2]) % 2 == 0:
        print('Sum of digits in even positions is even')
    else:
        print('Sum of digits in even positions is odd')


'''submit'''

## TEST (validate)
# q1aiii([1, 3, 2, 3])
# q1aiii([1, 2, 2, 3])

## 1b (i)
'''submit'''


def q1bi(strseq):
    for s in strseq[::-1]:
        print(int(s) - 1)


'''submit'''

## TEST
# q1bi('1204')

## 1b (ii)
'''submit'''


def q1bii(strval):
    for i in range(1, len(strval)):
        if int(strval[i - 1]) + int(strval[i]) > 12:
            return False
    return True


'''submit'''

##TEST
# print(q1bii('48531'))
# print(q1bii('11111'))

## q2 a
'''submit'''
## Proposed data strucuture to store product and price will be dictionary which the key will store the product name and value will store the price of the product.
## Example of proposed data structure.
xList = {'a': 1, 'b': 2, 'c': 3}
yList = {'a': 2, 'b': 4, 'c': 5}


## Example of proposed data structure for task 1
def q2aTask1(xList, yList):
    xValues = xList.values()
    yValues = yList.values()
    return (sum(xValues) / len(xValues)) - (sum(yValues) / len(yValues))


## Example of proposed data structure for task 2
def q2aTask2(xList, yList):
    ls = xList if len(xList) > len(yList) else yList
    for pro, pri in ls.items():
        xpri = xList.get(pro)
        ypri = yList.get(pro)
        if xpri is not None and ypri is not None and xpri < ypri:
            print(f'Product: {pro} Store X price: {xpri} Store Y price: {ypri}')


## Example of proposed data structure for task 3
def q2aTask3(prod, xList, yList):
    xpri = xList.get(prod)
    ypri = yList.get(prod)
    if xpri is not None and ypri is not None:
        print(f'Product: {prod} Store X price: {xpri} Store Y price: {ypri}')


'''submit'''

## TEST (validate)
# print('t1', q2aTask1(xList, yList))
# print('t2')
# q2aTask2(xList, yList)
# print('t3')
# q2aTask3('a', xList, yList)


## q2 b
'''
## Task 1: No control structure is required as we are using dictionary, we can make use of the length, values of dictionary and sum function to get the task done
def q2aTask1(xList, yList):
    xValues = xList.values()
    yValues = yList.values()
    return (sum(xValues) / len(xValues)) - (sum(yValues) / len(yValues))

## Task 2: Repetition control structure is required because we need to loop through each of the product to get the price before we can do any comparison. Thereafter we compare and return the result using selection statement
def q2aTask2(xList, yList):
    ls = xList if len(xList) > len(yList) else yList
    for pro, pri in ls.items():
        xpri = xList.get(pro)
        ypri = yList.get(pro)
        if xpri is not None and ypri is not None and xpri < ypri:
            print(f'Product: {pro} Store X price: {xpri} Store Y price: {ypri}')

## Task 3: Selection control struture is being used to ensure that both store contain the same product and thereafter we can output the result if and only if both store contain the same product
def q2aTask3(prod, xList, yList):
    xpri = xList.get(prod)
    ypri = yList.get(prod)
    if xpri is not None and ypri is not None:
        print(f'Product: {prod} Store X price: {xpri} Store Y price: {ypri}')
'''

## q3 a
import random


def roll():
    return sum([random.randint(1, 6) for i in range(3)])


'''submit'''

## TEST
# print(roll())


''' submit'''


## q3 b
def playGame(playerList, maxLimit):
    rolls = {}
    for player in playerList:
        val = roll()
        rolls[player] = val

    highest = None
    for p, v in rolls.items():
        if v < maxLimit:
            if highest is None:
                highest = v
            elif v > highest:
                highest = v

    winners = []
    for k, v in rolls.items():
        if v == highest:
            winners.append(k)
    return winners


''' submit'''

## TEST
# players = ['a', 'b', 'c']
# for i in range(10):
#     print(playGame(players, 10))

## q3 c
'''submit'''


def newLimit():
    while True:
        newLimit = int(input('Enter new max limit: '))
        if newLimit < 10:
            print('Please enter a number that is at least 10')
        else:
            return newLimit


def getOption():
    options = [
        '1. Change max limit for sum of 3 rolls',
        '2. Play Game',
        '0. Exit'
    ]

    print('Menu')
    for option in options:
        print(option)

    while True:
        opt = input('\nChoose your operation: ').strip()
        if opt in ''.join([str(i) for i in range(len(options))]):
            return int(opt)
        print('Invalid choice')


def main():
    playerList = ['A', 'B', 'C', 'D', 'E']
    maxLimit = 12

    while True:
        opt = getOption()

        if opt == 1:
            maxLimit = newLimit()

        elif opt == 2:
            print(', '.join(playGame(playerList, maxLimit)))

        else:
            break
    print('Application ends')


'''submit'''

## TEST
# main()

## 4a (i)
'''submit'''


def readProductData():
    products = {}
    with open('products.txt', 'r') as file:
        for line in file.readlines():
            code, price, name = line.split(',')
            products[code.strip()] = [float(price.strip()), name.strip()]
        file.close()
    return products


'''submit'''
## TEST
products = {'A020': [8.0, '137 Degree Real Almond Milk'], 'A121': [4.95, 'UFC Velvet Almond Milk'],
            'B123': [3.15, 'Wholemeal Bread'], 'B138': [5.95, 'Fruit and Nut Bread']}

# print(readProductData())


## 4a (ii)
'''submit'''


def getPrice(elem):
    return elem[1][0]


def saveToFile(products):
    '''Assuming that we are writing the file instead of appending'''
    with open('products.txt', 'w') as file:
        for prod, detail in dict(sorted(products.items(), key=getPrice)).items():
            file.write(f'{prod},{detail[0]},{detail[1]}\n')
        file.close()


'''submit'''

## TEST
# saveToFile(products)

## 4b (i)
'''submit'''


def getAndDisplayProducts():
    products = readProductData()
    for prod, detail in products.items():
        print(f'Code: {prod} ${float(detail[0]):,.2f} Name: {detail[1]}')


'''submit'''

## TEST
# getAndDisplayProducts()

## 4b (ii)
'''submit'''


def displayProducts(products):
    for prod, detail in products.items():
        print(f'Code: {prod} ${float(detail[0]):,.2f} Name: {detail[1]}')


def main():
    products = {'A020': [8.0, '137 Degree Real Almond Milk'], 'A121': [4.95, 'UFC Velvet Almond Milk'],
                'B123': [3.15, 'Wholemeal Bread'], 'B138': [5.95, 'Fruit and Nut Bread']}
    while True:
        code = input('Enter code of product: ').upper().strip()

        if len(code) == 0:
            print('Program ends')
            break
        else:
            price = float(input('Enter price of product: ').strip())
            if price > 0:
                if code in products:
                    products[code][0] = price
                    print(f'Updating entry {code} with new price {price:.2f}')
                else:
                    name = input('Enter name of product: ').strip()
                    products[code] = [price, name]
                    print(f'Adding entry {code}, {price:.2f}, {name} into products')
            else:
                print('Price must be positive value')
            print(products)


'''submit'''

## TEST
main()

