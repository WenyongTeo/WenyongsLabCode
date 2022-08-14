def main():
    num1 = int(input('Enter first number here: '))
    num2 = int(input('Enter second number here: '))
    sum =0
    if num1 <= num2:
        step = 1
    else:
        step = -1
    for i in range (num1,num2+step,step):
        sum += i
        print(i)

    print(f'sum is {sum}')

main()