from lib import getCharSet, getPositiveFloat

def bmiMenuOption():
    print("\nBMI Menu")
    print("========")
    print("(M) Calcualte BMI using Metric units")
    print("(I) Calcualte BMI using Imperial units")
    print("(F) Calcualte BMI using file input (Metrics) and display on screen")
    print(
        "(O) Calcualte BMI using file input (Metrics) and output to file on screen"
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
            pass
        else:  # option in "Oo":
            pass

    print("Bye bye")

main()