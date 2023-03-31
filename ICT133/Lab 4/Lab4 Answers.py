"""
6. (2 lists) A program is required to record and display the results of a swimming competition. The swimming pool has 5 lanes. The swimmer name for each lane is first recorded. After the race, the timings for the swimmers are captured. The results for the race is then displayed. Design a structure chart for this program.

a. Write a function inputSwimmers() that prompts for 5 swimmer names and returns the names in a list.  ["James", "Joseph", "Tom", "Dan", "Ian"]

An example of the input session is as follows:
    Enter lane 1 swimmer: James
    Enter lane 2 swimmer: Joseph
    …
    Enter lane 5 swimmer: Ian
Test the function.

b. Write another function inputTiming(swimmers) that has the list of swimmers names. The function creates an empty list, prompts and stores the timing for each of the swimmers. The timings list is returned. An example of the input session is as follows:   [47.15, 46.91, 48.2, 47.4, 48.01]
    Enter timing for James: 47.15
    Enter timing for Joseph: 46.91
    ….
    Enter timing for Ian: 48.01

c. Write another function printResults(swimmers, timings) that has the name and timing lists as parameters. The function prints a summary of the results as follows:
    James       47.15s
    Joseph      46.91s
    …
    Ian         48.01s
    Fastest is 46.91s
Assume all the timings are unique. Write a main function to test out all the parts in this question.

d. Modify the function in part c) that prints the summary in sorted order of the timing. Therefore, the summary may look like this:
    Joseph      46.91s
    James       47.15s
    …
    Ian         48.01s

Explore the sort(), sorted() function, or the zip() function to print the summary.
"""


def inputSwimmers(noOfSwimmers):
    swimmerList = []
    for i in range(1, noOfSwimmers + 1):
        name = input("Enter lane {} swimmer: ".format(i))
        swimmerList.append(name.title())

    return swimmerList


def inputTiming(swimmers):
    timingList = []
    for name in swimmers:
        timing = float(input("Enter timing for {}: ".format(name)))
        timingList.append(timing)

    return timingList


def printResults(swimmers, timings):
    # part(c)
    for s, t in zip(swimmers, timings):
        print("{:<15s} {:.2f}s".format(s, t))

    print("Fastest is {:.2f}s".format(min(timings)))

    # part(d)
    swimmerTimings = []
    for s, t in zip(swimmers, timings):
        swimmerTimings.append([t, s])  # [t,s] is [47.15, 'James'] ....  [48.01, 'Ian']

    # print(swimmerTimings)
    # swimmers = ["James", "Joseph", "Tom", "Dan", "Ian"]
    # timings =  [ 47.15,   46.91,    48.2,  47.4,  48.01]
    # [[47.15, 'James'], [46.91, 'Joseph'], [48.2, 'Tom'], [47.4, 'Dan'], [48.01, 'Ian']]
    # ===> nested list..... list within list... each element in the list is a list

    swimmerTimings.sort()
    # print(swimmerTimings)
    print("====")
    for element in swimmerTimings:  # element = [46.91, 'Joseph']
        print("{:<15s} {:.2f}s".format(element[1], element[0]))

    print("====")
    for t, s in swimmerTimings:  # t, s = [46.91, 'Joseph']
        print("{:<15s} {:.2f}s".format(s, t))


def lab4Q6():
    # swimmers = inputSwimmers(5)  # swimmers is a LIST
    swimmers = ["James", "Joseph", "Tom", "Dan", "Ian"]
    # timings = inputTiming(swimmers)
    timings = [47.15, 46.91, 48.2, 47.4, 48.01]
    printResults(swimmers, timings)


lab4Q6()

"""
5. (tuple, list) A test consists of 10 MCQ questions. Each question has 4 choices: a, b, c, d. The solution to each question is stored in a tuple as follows:

Q   1    2    3  .....                      9    10
  ('a', 'b', 'b', 'a', 'd', 'c', 'b', 'a', 'b', 'c')

to indicate that the answer to question 1 is a, to question 2 is b, etc.

Write a program that allows a user to take the quiz. The user is prompted for his answers to the 10 MCQ questions. Assume that the input will be one of the 4 valid choices: a, b, c, d. Store the answers in another collection.

After all the questions have been answered, the program displays if each of the questions is answered correctly, and if not, the program displays the correct answer.

A summary of the number of correct answers is also displayed.

An example run is shown here:
    Q1: a        ['a']   # keep appending
    Q2: b        ['a','b']
    Q3: c
    Q4: a
    Q5: d
    Q6: c
    Q7: b
    Q8: a
    Q9: d
    Q10: c
    Q1: a correct
    Q2: b correct
    Q3: c incorrect, answer is b
    Q4: a correct
    Q5: d correct
    Q6: c correct
    Q7: b correct
    Q8: a correct
    Q9: b correct
    Q10: c correct
    Total 9 out of 10 correct
"""
from myLib import getCharSet


def getAnswers(answers, noOfQuestions):
    # use a for loop to get answers from user
    for i in range(1, noOfQuestions + 1):
        userAnswer = getCharSet("Q{}: ".format(i), "abcdABCD")
        answers.append(userAnswer.lower())

    return


def checkSolution(solution, answers):
    # use a for loop to compare answers vs solution
    correct = 0
    for i in range(len(solution)):
        print("Q{}: {} ".format(i + 1, answers[i]), end="")
        if solution[i] == answers[i]:
            correct += 1
            print("correct")
        else:
            print("incorrect, answer is {}".format(solution[i]))

    print("Total {} out of {} correct".format(correct, len(solution)))


def lab4Q5():
    solution = ('a', 'b', 'b', 'a', 'd', 'c', 'b', 'a', 'b', 'c')
    answers = []
    getAnswers(answers, len(solution))
    # answers = ['a','b','b','a','a','c','b','a','b','c']
    # print(answers)
    checkSolution(solution, answers)
    """
    answers = getAnswers(len(solution))
    #answers = ['a','b','b','a','a','c','b','a','b','c']
    #print(answers)
    checkSolution(solution, answers)
    """


"""
Q4.
For example : NRIC No.(with official reference) = S7928964G

Step 1:
  Multiply each digit by the following weights.
    NRIC No. : 7  9  2  8  9  6  4
    Weights :  2  7  6  5  4  3  2
    Products: 14 63 12 40 36 18  8

  Make use of a tuple for the weights:
    weight = (2, 7, 6, 5, 4, 3, 2)

Step 2:
  Sum the products of each digit x weight.
  Sum : 14 + 63 + 12 + 40 + 36 + 18 + 8 = 191   ==> only S, F series
  for T and G series, add 4 to sum

Step 3:
  Find the remainder when the sum is divided by 11.
  Sum/11: 17 remainder 4

Step 4:
  Take 11 – remainder to get the check digit.
  Check digit : 11 – 4 = 7

Step 5:
  Look up the following table to get the official reference.
  Official Reference : G
  Conversion: (* A B C D E F G H I Z  J ) 
        Table  0 1 2 3 4 5 6 7 8 9 10 11
"""


def nricRefCheck(nric):
    weight = (2, 7, 6, 5, 4, 3, 2)
    reference = ('*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z', 'J')
    # processing, implement the above alogorithm
    # step 1 & 2
    total = 0
    for i in range(1, 8):
        product = int(nric[i]) * weight[i - 1]
        total = total + product

    if nric[0] in "TG":
        total = total + 4

    # step 3 & 4
    checkDigit = 11 - (total % 11)
    # print(checkDigit)

    # step 5
    # return (referenece[checkDigit] == nric[-1].upper())
    if reference[checkDigit] == nric[-1].upper():
        return True
    else:
        return False


def lab4Q4():
    nric = input('Enter NRIC: ').upper()

    # positive testing
    if len(nric) == 9:
        if nric[0] in 'STFG':
            if nric[1:8].isdigit():  # pos 1 to 7, exclude 8
                if nric[8].isalpha() and nricRefCheck(nric):
                    print("Valid NRIC")
                else:
                    print('Reference letter is invalid')
            else:
                print('Must consist of 7 digits')
        else:
            print('The first letter must be S, T, F or G')
    else:
        print('Length must be exactly 9')


"""
3. (List) Write a program to record the statistics of 100 throws of a dice. Use an initial list as follows to record the occurrences of each value of the dice:

        diceCount = [0, 0, 0, 0, 0, 0, 0]

The element at index 0 of the list will not be used. When the dice value is 1, add 1 to index 1 of the list etc. After 100 throws of the dice, display a summary of the occurrences of the dice values as follows:

        Dice Occurrence
        1 16
        2 14
        3 15
        4 17
        5 18
        6 20
        Total 100

# TOP-DOWN DESIGN
diceCount = [0, 0, 0, 0, 0, 0, 0]
loop 100 times
    value = rolldice()
    add 1 to diceCount[value]
displaySummary()
"""
from random import randint
from myLib import getPositiveInteger


def rollDice():
    return randint(1, 6)


def displaySummary(stats):
    print("Dice Occurrence")
    for i in range(1, 7):
        print("{}    {}".format(i, stats[i]))

    print("Total: {}".format(stats[0]))


def lab4Q3():
    diceCount = [0, 0, 0, 0, 0, 0, 0]
    diceCount[0] = getPositiveInteger("Enter no of throws: ")

    for i in range(diceCount[0]):
        diceValue = rollDice()
        diceCount[diceValue] += 1  # increment by 1

    displaySummary(diceCount)


"""
lab4 Q2
"""

from myLib import getCharSet, getPositiveFloat


def bmiMenuOption():
    print("\nBMI Menu")
    print("========")
    print("(M) Calcualte BMI using Metric units")
    print("(I) Calcualte BMI using Imperial units")
    print("(F) Calcualte BMI using file input (Metrics) and display on screen")
    print(
        "(O) Calcualte BMI using file input (Metrics) and output to file"
    )
    print("(X) Exit")
    choice = getCharSet("Enter your choice : ", "MmIiFfOoXx")
    return choice


def bmiCalculator(weight, height):
    return weight / (height * height)


def bmiRating(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "normal"
    elif bmi >= 25 and bmi < 30:
        return "overweight"
    else:
        return "obese"


def performMetric():
    height = getPositiveFloat("Please enter your height in meters : ")
    weight = getPositiveFloat("Please enter your weight in kg : ")
    showBMIOutcome(weight, height)


def performImperial():
    height = getPositiveFloat("Please enter your height in inches : ")
    weight = getPositiveFloat("Please enter your weight in pounds : ")
    weight = weight * 703
    showBMIOutcome(weight, height)


def showBMIOutcome(weight, height):
    bmi = bmiCalculator(weight, height)
    rating = bmiRating(bmi)
    print("Your BMI is {:.2f} which means you are {}.".format(bmi, rating))


def lab4Q2a():
    infile = open("customer.dat", "r")
    print("{:<15s} {:<8s} {:<8s} {:<8s}".format("Name", "Weight", "Height", "BMI"))

    for line in infile:
        name, weight, height = line.split(',')  # the 3 are still string!!!
        bmi = bmiCalculator(float(weight), float(height))
        print("{:<15s} {:<8.2f} {:<8.2f} {:<8.2f}".format(name, float(weight), float(height), bmi))

    infile.close()


def lab4Q2b():
    infile = open("customer.dat", "r")
    outfile = open("bmi.dat", "a")
    print("{:<15s} {:<8s} {:<8s} {:<8s}".format("Name", "Weight", "Height", "BMI"), file=outfile)

    for line in infile:
        name, weight, height = line.split(',')  # the 3 are still string!!!
        bmi = bmiCalculator(float(weight), float(height))
        print("{:<15s} {:<8.2f} {:<8.2f} {:<8.2f}".format(name, float(weight), float(height), bmi), file=outfile)

    print("Done... check bmi.dat")
    infile.close()
    input()


def main():
    while True:
        option = bmiMenuOption()

        if option in "Xx":
            break
        elif option in "Mm":
            performMetric()
        elif option in "Ii":
            performImperial()
        elif option in "Ff":
            lab4Q2a()
        else:  # option in "Oo":
            lab4Q2b()

    print("Bye bye")


"""
Lab4 Q1
The rainfall (in mm) for each day in a particular month is captured in a file, rainfall.dat. Write a program to read the rainfall for each day, and display a summary report as follows:

    Rainfall Summary
    Average rainfall 5.65mm
    No of days with no rain 3 days
    Highest rainfall recorded 20.6mm
"""


def lab4Q1():
    # intro to reading file
    infile = open("rainfall.dat", "r")

    totalRainfall = 0
    days, noRainDays, highestRainfall = 0, 0, 0
    for reading in infile:
        days += 1
        rainfall = float(reading)  # converting to float get rid of \n too
        totalRainfall = totalRainfall + rainfall  # accumulating
        if rainfall == 0:  # check no day?
            noRainDays += 1
        else:
            if rainfall > highestRainfall:
                highestRainfall = rainfall

    print("Rainfall Summary")
    print("Average rainfall {:.2f}mm".format(totalRainfall / days))
    print("No of days with no rain {} days".format(noRainDays))
    print("Highest rainfall recorded {:.1f}mm".format(highestRainfall))

    infile.close()

