from art import logo
import random

def get_random_number():
    return random.randint(1,100)

def is_too_low_or_high():
    global number_of_attempts
    guess = int(input("Make a guess: "))
    number_of_attempts-=1
    if guess < number:
        print("Too low.")
        print("Guess again.")
    elif guess > number:
        print("Too high.")
        print("Guess again.")
    else:
        print(f"You got it! The answer was {number}.")
        quit()
    print_number_of_attempts()

def print_number_of_attempts():
    if number_of_attempts>0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses, you lose.")
        quit()

number_of_attempts = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = get_random_number()
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    number_of_attempts = 10
elif difficulty == "hard":
    number_of_attempts = 5
else:
    print("Invalid input!")
    quit()

print(f"You have {number_of_attempts} attempts remaining to guess the number.")
while 0 < number_of_attempts:
    is_too_low_or_high()