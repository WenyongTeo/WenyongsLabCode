"""
Lab2 Q5 & Q8
(if…elif…else) Modify the program in question 5 with the following rate:

  Data           Rate
  Up to 2GB      $5 flat
  Above 2GB      $5 + $1 for every 100MB or part thereof
  Above 4GB      $25 flat

The program also validates that input must be greater than 0. Otherwise, display “Invalid input!”.
"""
import math


def main():
    data = float(input('Amount of data used (GB): '))

    if data <= 0:
        print("Invalid input!")
    else:

        if data <= 2:
            charge = 5
        elif 2 < data <= 4:
            # do integer division for better precison
            charge = math.ceil(5 + ((data * 1000 - 2000) / 100))
        else:  # data > 4
            charge = 25

        print("Charge is ${:.2f}".format(charge))