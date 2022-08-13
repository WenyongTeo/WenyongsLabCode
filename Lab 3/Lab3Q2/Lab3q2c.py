'''
(while, sentinel) Modify program for 2a so that it repeatedly
prompts for another string to process
until the user keys in “exit” to end the program.
E.g.,Enter String: Python
Number of times to repeat: 3
Python
Python
Python
Enter String: program
Number of times to repeat: 2
program
program
Enter String: exit
end
'''

def main():
    while True:
        word = input('Word: ')
        if word in 'Exit':
            print("STOP!")
            break

        num = int(input("Times "))
        for i in range(num):
            print(word)
main()

