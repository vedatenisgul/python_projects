import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock,paper,scissors]

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(rock_paper_scissors[option])
print("Computer chose:")

random_number = random.randint(0,2)
print(rock_paper_scissors[random_number])
if option == random_number:
    print("It is a tie.")
elif (option == 2 and random_number == 0) or (option == 0 and random_number == 1) or (option == 1 and random_number == 2):
    print("You lose.")
else:
    print("You win.")