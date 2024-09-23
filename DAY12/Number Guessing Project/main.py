# import random
#
# number =  random.randint(1,100)
#
# print("Welcome to the Number Guessing Game :)")
# mode = input("Please choose a mode: Easy? or Hard?").lower()
#
# lives = 0
#
# if mode == "easy":
#     lives = 10
# elif mode == "hard":
#     lives = 5
#
# game = True
#
# while lives > 0 and game == True:
#     guess = int(input("Enter a Number: "))
#     if guess > number:
#         lives -= 1
#         print(f"Too High. {lives} lives left\n")
#     elif guess < number:
#         lives -= 1
#         print(f"Too Low. {lives} lives left\n")
#     else:
#         print("You guessed right!")
#         game = False
#
# if lives == 0:
#     print(f"You are out of lives. The number was {number}")

import random

EASY_LIVES = 10
HARD_LIVES = 5

def difficulty():
    mode = input("Please choose a mode: Easy? or Hard?").lower()
    if mode == "easy":
        return EASY_LIVES
    elif mode == "hard":
        return HARD_LIVES

def check_guess(lives):
    game = True
    while lives > 0 and game == True:
        guess = int(input("Enter a Number: "))
        if guess > number:
            lives -= 1
            print(f"Too High. {lives} lives left\n")
        elif guess < number:
            lives -= 1
            print(f"Too Low. {lives} lives left\n")
        else:
            print("You guessed right!")
            game = False
    if lives == 0:
        print(f"You are out of lives. The number was {number}")

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game :)")

guesses = difficulty()
check_guess(guesses)