from hangmanart import logo,stages
from hangmanword import word_list
from random import choice


randomWord = choice(word_list)
display = []
for i in range(len(randomWord)):
    display+="_"


lives= len(stages)-1

print(randomWord)
while lives < 7:
    guess = input("Enter your guess word (A-Z):").lower()
    if guess in display:
        print(f'You already guessed the word {guess}')
    for position in range(len(randomWord)):

        if guess == randomWord[position]:
            display[position] = randomWord[position]
            print(f'The word {guess} you guessed is Right!')

    print(display)
    print(stages[lives])
    if guess not in randomWord:
        print(f'The word {guess} you guessed is wrong!')
        lives-=1

        if lives == 0:
            print('You lose')
            break
    if "_" not in display:
        print('You win!')
        break