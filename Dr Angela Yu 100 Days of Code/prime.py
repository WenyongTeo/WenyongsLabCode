def prime_checker(number):
    isPrime = True
    for i in range(2,number):
        if number % i==0:
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)