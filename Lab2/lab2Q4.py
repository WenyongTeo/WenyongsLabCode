#(String, if…else) Write a program that reads a string and checks whether it is a palindrome.
#It displays either the message palindrome or the message not a palindrome.
#A palindrome is a word that spells the same backwards, e.g., the word solos is a palindrome.

def main():
    wordCheck= input('Enter the word: ')
    if wordCheck.upper() == wordCheck[::-1].upper() :
        print('It is a palindrome')
    else:
        print('It is not a palindrome')


main()