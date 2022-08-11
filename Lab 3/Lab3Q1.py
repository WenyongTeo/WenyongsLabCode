def main():
    n1= int(input("Enter first number "))
    n2= int(input("Enter second number "))
    for i in range (n1, n2+1,1):
        print(i)

    sum= 0
    for i in range(n1, n2+1):
        sum+=i
        print(i)
    print(f"sum of them is {sum}")
main()
