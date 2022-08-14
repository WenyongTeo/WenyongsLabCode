#Write a function sumSquares(num) that has 1 integer parameter.
# The function returns the sum of the squares from 1 up to num.
# E.g. sumSquares(4) returns the sum of 12+22+32+42. Test the function.
#answers below
'''
the function returns the sum of the squares from 1 up to num
'''
def sumSquares(num):

    sumOfSquares = 0
    for i in range(1,num+1):
        sumOfSquares= sumOfSquares +(i**2)
    return sumOfSquares

def main():
    number = int(input('Enter the number to compute sum squares'))
    results = sumSquares(number)
    print(f'Sum for square {number,results}')
main()


























'''
def sumSqure(num):
    sumofSqu= 0
    for i in range(1,num+1):
        sumofSqu = sumofSqu + i*i
    return sumofSqu



def main():
    number = int(input("enter number "))
    result = sumSqure(number)
    print('sum of square {} = {}'.format(number,result))
main()
'''