#Modify program in 1b to cater for any 2 integer input sequence.
#If the first is smaller than the second, print from the smaller to larger.
#If the first is greater than the second, print from the larger down to the smaller.
#Use only 1 loop structure for the printing.
#if num1 > num2, increment 1, if num2 > num1, increment -1
def main():
    num1 = int(input('Enter first number here: '))
    num2 = int(input('Enter second number here: '))
    sum =0
    if num1 > num2:
        for i in range (num1,num2-1,-1):
            print(i)
            sum += i
        print(f'sum is {sum}')
    else:
        for i in range (num1,num2+1,1):
            print(i)
            sum += i
        print(f'sum is {sum}')

main()