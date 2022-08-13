'''
(while, sentinel loop) Write a program that displays the menu shown in the example run repeatedly until the user chooses 0 to quit.
You may assume that user enters only valid numbers (0-3).
'''
def main():
    while True:
        print('Menu\n''1. Option 1\n''2. Option 2\n''3. Option 3\n''0. Quit')
        select= int(input("Enter Choice: "))
        print(f'Option {select} selected')
        if select == 0:
            break
    print('End of program')

main()
