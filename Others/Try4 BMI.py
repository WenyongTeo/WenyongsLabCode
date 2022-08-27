def main():
    w= float(input("Enter your weight here "))
    h= float(input("Enter your height here "))
    bmi= w / (h * h)
    print(f'Your BMI is {bmi:.2f}')
    if bmi < 18.5:
        print("underweight")
    elif bmi >=18.5 and bmi <=24.9:
        print("Healthy Weight")
    elif bmi >= 25 and bmi <=29.9:
        print("Overweight")
    else:
        print("Obsese")

from random import randint


def computerChoice():
  aiChoice = ['Rock', 'Paper', 'Scissor']
  threeChoice = len(aiChoice)
  randomChoice = randint(1,threeChoice)
  return randomChoice
def main():
  print(computerChoice())
main()
