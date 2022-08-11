
def main():
    side1 = float(input("Enter side 1 here "))
    side2 = float(input("Enter side 2 here "))
    side3 = float(input("Enter side 3 here "))

    s = side1 + side2

    if (side1 + side2 <= side3) or (side3 + side2 <= side1) or (side1 + side3 <= side2):
        print("Bruh this aint a triangle")

    elif side1 == side2 == side3:
        print("All three sides are equal, Equilateral")

    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Any two sides are equal, Isosceles")

    else:
        print('All 3 are unequal , Scalene')

main()
