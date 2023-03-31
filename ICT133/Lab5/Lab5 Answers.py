'''# lab5 Q4
from myLib import getIntegerRange, getPositiveFloat, getCharSet


def menuOption():
    print("Menu")
    print("1. Add student")
    print("2. Adjust marks")
    print("3. Remove student")
    print("4. Display marks")
    print("0. Quit")
    option = getIntegerRange("Enter choice: ", 0, 4)
    return option


def addStudent(marks):
    # always search for the key before accessing the dictionary
    name = input("Enter student name to add: ").capitalize()
    if name in marks:  # try to match the keys
        print("Student {} already exist!!".format(name))
    else:
        cw = getPositiveFloat("Enter coursework: ")
        ex = getPositiveFloat("Enter exam: ")
        marks[name] = [cw, ex]  # make cw,ex into a list by [ ]
        print("Added...")


def updateMarks(marks):
    # always search for the key before accessing the dictionary
    name = input("Enter student name to adjust: ").capitalize()
    if name in marks:  # try to match the keys
        currentScore = marks[name]  # give me [60,40]
        print("Coursework/Exam is {:.1f}/{:.1f}".format(currentScore[0], currentScore[1]))
        choice = getCharSet("Update C or E: ", "CcEe")
        if choice in "Cc":
            currentScore[0] = getPositiveFloat("Enter coursework: ")
        else:
            currentScore[1] = getPositiveFloat("Enter exam: ")
        print("Update")
    else:
        print("No such student!")


def removeStudent(marks):
    # always search for the key before accessing the dictionary
    name = input("Enter student name to remove: ").capitalize()
    if name in marks:  # try to match the keys
        del marks[name]
        print("Student {} removed!!".format(name))
    else:
        print("No such student!")


def displayMarks(marks):
    print("\n{:8s} {:4s}  {:4s} {:7s} {:5s}".format("Name", "Cw", "Exam", "Overall", "Grade"))
    for k, v in marks.items():  # items() give you k,v
        # v is [60,40]
        overall = sum(v) / 2  # v[0] + v[1]
        if overall >= 50:
            grade = 'P'
        else:
            grade = 'F'
        print("{:8s} {:4.1f}  {:4.1f} {:7.1f} {:^5s}".format(k, v[0], v[1], overall, grade))
    print()


def main():
    # 4a - setup a dictionary of ccy and fx rate
    marks = {'John': [60, 40], 'Jane': [50, 50], 'Peter': [60, 70], 'Joe': [30, 50]}

    while True:
        option = menuOption()
        if option == 0:
            break
        elif option == 1:
            addStudent(marks)
        elif option == 2:
            updateMarks(marks)
        elif option == 3:
            removeStudent(marks)
        else:
            displayMarks(marks)

    print("bye")


main()

# lab5 Q3

rom
myLib
import getIntegerRange, getPositiveFloat


def menuOption():
    print("Menu")
    print("1. Add Currency")
    print("2. Adjust Currency")
    print("3. Remove Currency")
    print("4. Display Currency rates")
    print("0. Quit")
    option = getIntegerRange("Enter choice: ", 0, 4)
    return option


def addCurrency(currs):
    # always search for the key before accessing the dictionary
    ccy = input("Enter ccy to add: ").upper()
    if ccy in currs:  # try to match the keys
        print("currency {} already exist!!".format(ccy))
    else:
        rate = getPositiveFloat("Enter rate: ")
        currs[ccy] = rate
        print("Currency {} with rate {:.2f} added...".format(ccy, rate))


def adjustCurrency(currs):
    # always search for the key before accessing the dictionary
    ccy = input("Enter ccy to adjust: ").upper()
    if ccy in currs:  # try to match the keys
        print("Current rate is {:.2f}".format(currs[ccy]))
        newRate = getPositiveFloat("Enter new rate: ")
        currs[ccy] = newRate
        print("Currency {} adjusted to {:.2f}".format(ccy, newRate))
    else:
        print("Currency {} not found!!".format(ccy))


def removeCurrency(currs):
    # always search for the key before accessing the dictionary
    ccy = input("Enter ccy to remove: ").upper()
    if ccy in currs:  # try to match the keys
        del currs[ccy]
        print("Currency {} removed!!".format(ccy))
    else:
        print("Currency {} not found!!".format(ccy))


def displayCurrencyRate(currs):
    print("\n{:8s}   {:4s}".format("Currency", "Rate"))
    for k, v in currs.items():  # items() give you k,v
        print("{:<8s}   {:<4.2f}".format(k, v))
    print()


def main():
    # 3a - setup a dictionary of ccy and fx rate
    currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}

    while True:
        option = menuOption()
        if option == 0:
            break
        elif option == 1:
            addCurrency(currs)
        elif option == 2:
            adjustCurrency(currs)
        elif option == 3:
            removeCurrency(currs)
        else:
            displayCurrencyRate(currs)

    print("bye")


# lab5 Q2
def getPlayerNames():
    gameScoreList = []
    p1Name = input("Enter 1st player name: ")
    p2Name = input("Enter 2nd player name: ")
    gameScoreList.append([p1Name, p2Name])
    return gameScoreList  # [ [p1Name,p2Name] ]


def inputGamesScores(scoreList):
    p1Name, p2Name = scoreList[0][0], scoreList[0][1]
    gameNo = 1
    while True:
        inputScore = input("Game {} score {} vs {}: ".format(gameNo, p1Name, p2Name))
        if inputScore == "":  # = <enter> ?
            break

        gameNo += 1
        p1Score, p2Score = inputScore.split("-")
        scoreList.append([int(p1Score), int(p2Score)])


def displayGameScore(gameScore):
    # gameScore[0] = ['A','B']
    print("Player {} vs {}".format(gameScore[0][0], gameScore[0][1]))
    p1Score, p2Score = 0, 0
    for i in range(1, len(gameScore)):
        print("Game {}: {}-{}".format(i, gameScore[i][0], gameScore[i][1]))
        if gameScore[i][0] > gameScore[i][1]:
            p1Score += 1
        else:
            p2Score += 1

    print("Overall {}-{}".format(p1Score, p2Score))
    if p1Score > p2Score:
        winner = gameScore[0][0]
    else:
        winner = gameScore[0][1]
    print("Winner is player {}".format(winner))


def lab5Q2():
    gameScore = getPlayerNames()
    # gameScore = [['A','B']]
    inputGamesScores(gameScore)
    # gameScore = [['A','B'],[21,1],[21,10]]
    # gameScore = [['A','B'],[21,11],[19,21],[20,22]]
    displayGameScore(gameScore)'''