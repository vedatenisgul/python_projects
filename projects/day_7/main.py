from hangman_words import word_list
from hangman_art import stages,logo
from os import system
import random

#choose a random word from hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)

#for test purposes
print(f'Pssst, the solution is {chosen_word}.')

#create blanks
display = ["_"] * len(chosen_word)

while "_" in display and lives>0:
    guess = input("Guess a letter: ").lower()
    #clear screen
    system("clear")

    #check if user enters repeated input
    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #print stages of hangman
    print(stages[lives])

    if lives == 0:
        print("You lose.")


    #Check if user has got all letters.
    if "_" not in display:
        print("You win.")


    