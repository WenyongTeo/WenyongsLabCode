''''
#(for loop) Write a program that displays a multiplication table.
Read an integer number and display the multiplication table as
follows in this example run:
Enter number: 5
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
If the input is 5, the table displays 5 rows,
each row for a multiple of 5.
'''
def main():
    num= int(input('Enter number here: '))
    for i in range(num):
        print(f'{i+1}x{num}={(i+1)*num}')
main()