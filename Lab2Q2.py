#2. (String) Write a program that reads in a string input consisting of 2 words with a blank in between.
# The program displays each of the word in reverse. Example:
#Enter string: java python
#Output: avaj nohtyp
#Assume input is valid.

def reverse():
   word1, word2= input('Enter words:').split(' ')
   print('Reverse is:{}'.format(word1[::-1]), '{}'.format(word2[::-1]))

reverse()
