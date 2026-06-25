import random

user_choice = input("rock, paper, scissor?: ").lower()
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissor
}


if user_choice == "rock":
    print(f"You chose rock.\n\n{rock}\n\nComputer chose {computer_choice}.")
    print(choices_art[computer_choice])
    if computer_choice == "paper":
        print("You Lose!")
    else:
        print("You Win!")
elif user_choice == "paper":
    print(f"You chose rock.\n\n{paper}\n\nComputer chose {computer_choice}.")
    print(choices_art[computer_choice])
    if computer_choice == "scissor":
        print("You Lose!")
    else:
        print("You Win!")
elif user_choice == "scissor":
    print(f"You chose rock.\n\n{scissor}\n\nComputer chose {computer_choice}.")
    print(choices_art[computer_choice])
    if computer_choice == "rock":
        print("You Lose!")
    else:
        print("You Win!")