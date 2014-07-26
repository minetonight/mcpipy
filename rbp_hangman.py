"""took 43 min to develop on a tablet"""
import random
  
words = ["implementation"]

word = words[random.randint(0, 0)]
tries = 0
guess = ""

while tries < 10:

    for letter in range(len(word)):
        if word[letter] == guess:
            print( word[letter] ),
        else:
            print("_"),
            
    guess = raw_input("guess a letter")
    tries += 1
    
guess = raw_input("No more guesses, which one is the word? ")
if word == guess:
    print("You win. You live!")
else:
    print("You lose. Hanged!")
