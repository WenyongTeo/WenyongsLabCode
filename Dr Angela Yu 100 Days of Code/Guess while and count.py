import random
word_list = ['Apple','Samsung','Oppo']
count = 1
win = 0
while count < 4:
    randomWord = random.choice(word_list)
    print(randomWord)
    guess = input(f"Guess {count } Enter your choice of word:")
    if randomWord == guess.lower():
        print("Correct choice!")
        win+=1
    else:
        print('Wrong!')
    count+=1
print(f"You guessed correctly {win} times!")