#Project 8: Hangman Game

import random
words = ['doctor', 'python', 'code', 'ai', 'abdullah']
word = random.choice(words)
guessed_letters = []
attempts = 8

print("Welcome to the game!!!")
print("_" * len(word))

while attempts > 0:
    guess = input("\n guess the letters:  ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Enter 1 Alphabet only: ")
        continue
    if guess in guessed_letters:
        print("This letter is Guessed!!! Try another letter")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        print("Correctly Guess")
    else:
        attempts -= 1
        print(f'Wrong {attempts} attempts')
        
    displayed_word = "  ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)
    
    if "_" not in displayed_word:
        print(f"Yahoooo!!! Congratulations... You won the game. The correct word is : {word}")
        break
else:
    print(f"Oooops!!!! You lose... GAme over. The correct word is : {word}")