from game_data import data
import random
import art

def compare(num1, num2):
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0


a = random.choice(data)
b = random.choice(data)
score = 0
game = True

print("WELCOME TO")

while game:
    while a == b:
        b = random.choice(data)

    print(art.logo)
    print(f"A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"B: {b['name']}, a {b['description']}, from {b['country']}")
    choice = input("Who has more followers? A or B? ").lower()

    if choice == "a":
        choice = 1
    elif choice == "b":
        choice = -1


    if choice == compare(a["follower_count"],b["follower_count"]):
        a = b
        b = random.choice(data)
        score += 1
        print("\n" * 20)
        print(f"That's correct! Your current score is {score} points.")
    else:
        print(f"That's incorrect! Your final score is {score} points.")
        game = False