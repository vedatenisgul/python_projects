from art import logo
from os import system
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0
cards_list = {"user":user_cards,"computer":computer_cards}

def calculate_score(who):
    #Calculates the score for the given player, handling Aces as 1 or 11.
    score = sum(cards_list[who])  # Sum the card values directly
    
    # Adjust for Aces if over 21
    while score > 21 and 11 in cards_list[who]:
        cards_list[who].remove(11)
        cards_list[who].append(1)
        score -= 10

    return score

def who_win():
    #Determines and prints the winner of the game.
    if computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > user_score:
        print("You lose 😤")
    elif computer_score < user_score:
        print("You win 😃")
    else:
        print("Draw")

def reset_game():
    global user_cards, computer_cards, user_score, computer_score
    user_cards.clear()
    computer_cards.clear()
    user_score = 0
    computer_score = 0

def print_scores():
    #print current scores
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards}")

def get_random_card(who):
    global user_score, computer_score  # Access the global variables
    cards_list[who].append(random.choice(cards))
    
    # Update the correct score variable based on who is playing
    if who == "user":
        user_score = calculate_score(who)
    elif who == "computer":
        computer_score = calculate_score(who)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    system("clear")
    print(logo)
    
    reset_game() #reset game
    #randomly selecting cards for both computer and user
    user_cards.extend(random.choices(cards,k=2))
    get_random_card("computer")
    user_score = calculate_score("user")

    print_scores()
    while True:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_another_card == "n":
            while computer_score<17:
                get_random_card("computer")
            break
        elif get_another_card == "y":
            get_random_card("user")
            print_scores()
            if user_score > 21:
                get_random_card("computer")
                break

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    who_win()

