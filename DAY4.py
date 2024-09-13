import random

print("Welcome to Rock Paper Scissors!")

options = ["rock","paper","scissors"]

computer = random.choice(options)

player = input("Pick rock, paper or scissors\n").lower()

print(f"\n\nComputer picked {computer}\n\nYou picked {player}\n\n")

if player == "rock":
    if computer == "rock":
        print("ITS A DRAW")
    elif computer == "scissors":
        print("YOU WIN")
    else:
        print("YOU LOSE")

if player == "scissors":
    if computer == "rock":
        print("YOU LOSE")
    elif computer == "scissors":
        print("ITS A DRAW")
    else:
        print("YOU WIN")

if player == "paper":
    if computer == "rock":
        print("YOU WIN")
    elif computer == "scissors":
        print("YOU LOSE")
    else:
        print("ITS A DRAW")