#This is for testing codes
'''5. Write a program that reads an input representing a change which is an amount less than 1 dollar.
The program calculates the change into 50, 10, 5 and 1 cent coins.
The program then displays the number of each coin required for that change. E.g.
Enter change: 47      87     101
50 cent: 0             1       2
10 cent: 4             3       0
5 cent: 1              1       0
1 cent: 2              2       1'''

def q5():
    change= input(int("Enter Change: "))
    cent50 = change//50
    cent10 = change%50//10
    cent5 = change%10//5
    cent1= change%5//1

q5()