from art import logo, vs
import random
from game_data import data
import os


def random_person() -> dict:
    if len(data)== 0:
        print("Congratz! You finished the game.")
        quit()
    person = random.choice(data)
    data.remove(person)
    return person

def has_more_followers(choice: str, compare_A: dict, compare_B: dict) -> bool:
    choice = choice.lower()
    if choice == "a":
        return compare_A["follower_count"] > compare_B["follower_count"]
    elif choice == "b":
        return compare_A["follower_count"] < compare_B["follower_count"]
    else:
        quit()

def print_persons(compare_A: dict, compare_B: dict) -> None:
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(vs)
    print(f"Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")

next_person = random_person()
score = 0

while True:
    print(logo)
    compare_A = next_person
    compare_B = random_person()
    
    if score > 0:
        print(f"You're right! Current score: {score}")
    
    print_persons(compare_A, compare_B)
    
    choice = input("Who has more followers? Type 'A' or 'B': ")
    is_correct = has_more_followers(choice, compare_A, compare_B)
    
    os.system("cls" if os.name == "nt" else "clear")
    
    if not is_correct:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    else:
        next_person = compare_B
        score += 1
