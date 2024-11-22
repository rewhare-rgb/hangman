# a random word is chosen for the player to guess

# the player guesses letters, one at a time

# if a letter is correct, it is revealed in the word

# if incorrect, the player loses a life

# the game ends when the word is guessed or lives are lost

import random
from words import words

def get_word():
    return random.choice(words).upper()

def free_hint(word, hidden_word):
    random_index = random.choice([i for i, letter in enumerate(word) if hidden_word[i] == "_"])
    hidden_word[random_index] = word[random_index].upper()
    return hidden_word


word = get_word()


guessed_letters = []
hidden_word = ["_" for letter in word]
lives = 6

print(f"Welcome to Hangman! You have {lives} lives.")
print("The word is:", " ".join(hidden_word))

use_hint = input("Would you like to use a free hint to reveal one letter? (y/n): ").lower()

if use_hint == "y":
    hidden_word = free_hint(word, hidden_word)
    print(f"Here is your free hint: ", " ".join(hidden_word))

while lives > 0:
    guess = input("Guess a letter: ").upper()
    
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
            print("Correct! Current word:", " ".join(hidden_word))
        else:
            guessed_letters.append(guess)
            lives -= 1
            print(f"Incorrect guess. You have {lives} {'life' if lives == 1 else 'lives'} remaining.")
            print("Current word:", " ".join(hidden_word))

    else:
        print("Invalid input. Please enter a letter from the alphabet.")

    if "_" not in hidden_word:
        print("Congratulations! You guessed the word:", word.upper())
        break

if lives == 0:
    print(f"Game over! The word was: {word.upper()}")

