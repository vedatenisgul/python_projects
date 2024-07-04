from art import logo
from os import system
import sys

def find_highest(bidding_data):
    highest_bid = 0
    highest_bid_owner = ""
    for key in auction_data:
        if auction_data[key] > highest_bid:
            highest_bid = auction_data[key]
            highest_bid_owner = key
    print(f"The winner is {highest_bid_owner} with a bid of ${highest_bid}")

print(logo)
print("Welcome to the secret auction program.")
finish_auction = False
auction_data = {}
while not finish_auction:
    participant_name = input("What is your name? ")
    participant_bid = int(input("What's your bid? $"))
    auction_data[participant_name] = participant_bid
    are_there_other_participants = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if are_there_other_participants == "no":
        finish_auction = True
    elif are_there_other_participants == "yes":
        system("clear")
    else:
        print("Invalid input!")
        sys.exit()

find_highest(auction_data)


