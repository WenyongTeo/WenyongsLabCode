#Modify the program to display the sum of the
# consecutive numbers after the consecutive numbers
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input('Enter second number: '))
    sum = 0
    for i in range(num1,num2+1):
        print(i)
        sum += i
    print(f"Sum of the range is {sum}")


main()
