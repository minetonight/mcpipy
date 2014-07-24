#started 22:50
import random

words = ["implementation"]

word = words[random.randint(0, 0)]

letters = []

#for index in range(len(word)):
#    letters[index] = word

tries = 0
guess = ""

while tries < 10:

    for index in range(len(word)):
        if word[index] == guess:
            print( word[index] ),
        else:
            print("_"),
            
    guess = raw_input("guess a letter")
    tries += 1
    
guess = raw_input("No more guesses, which one is the word? ")
if word == guess:
    print("You win. You live!")
else:
    print("You lose. Hanged!")
    
    
#working at 23:33 on tablet