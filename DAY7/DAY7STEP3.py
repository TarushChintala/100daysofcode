import random
word_list = ["aardvark","camel","baboon"]

word = random.choice(word_list)

placeholder = ""

for i in word:
    placeholder += "_"
print(placeholder)

game_over = False
correct = []
while not game_over:
    choice = input("Guess a letter:\n").lower()

    display = ""

    for letter in word:
        if choice == letter:
            display += choice
            correct.append(choice)
        elif letter in correct:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("YOU WIN")