import random
from collections import Counter

progLanguages = '''python javascript c++ dart php sql r c# go java react flutter'''
progLanguages = progLanguages.split(' ')
pickedLang = random.choice(progLanguages)
print('Guess the word! HINT: It is a programming language')
for letter in pickedLang:
    print('_', end=' ')
print('\n\n')
chances = len(pickedLang) + 2
won = False
lettersGuessed = ''
while chances and not won:
    print('\nYou have', chances, 'chances left, and you will lose chances only if you made wrong guesses\n')
    # input a guess from user
    guess = input('Guess a letter:\t')
    # validation of the guess
    if guess.isdecimal():
        print('You should Enter only A letter or a special character')
    elif len(guess) > 1:
        print('You should Enter a single letter')
    elif guess in lettersGuessed:
        print('You already guessd that letter before')
    # if he guessed a correct letter
    elif guess in pickedLang:
        noOfAppearances = pickedLang.count(guess)
        # save the guess
        # and the number of it's appearances
        for i in range(noOfAppearances):
            lettersGuessed += guess
        for letter in pickedLang:
            if letter in lettersGuessed and Counter(pickedLang) != Counter(lettersGuessed):
                print(letter, end = ' ')
            elif Counter(pickedLang) == Counter(lettersGuessed):
                # user won
                print('\nThe word is', pickedLang)
                print('\nCongrats you won')
                # terminate while loop
                won = True
                # break the for loop
                break
            else:
                print('_', end = ' ')
       
    else:
        for letter in pickedLang:
            if letter in lettersGuessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        chances -= 1
            
    
# display a losing message in case user lost
if chances == 0 and not won:
    print('\n\nYou lost as you are out of chances, Better luck next time!!')
    print('\nThe word was', pickedLang)
            