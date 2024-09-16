import random

stages = ['''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
 ____|____
''',
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|____
''',
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|____
''',
'''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |       
     |
 ____|____
''',
'''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 ____|____
''',
'''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|____
''',
'''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|____
''' 
]
word_list = ["aardvark","camel","baboon"]

word = random.choice(word_list)

placeholder = ""

for i in word:
    placeholder += "_"
print(placeholder)
lives = 6
game_over = False
correct = []
while not game_over:
    print(stages[lives])
    choice = input("Guess a letter:\n").lower()

    display = ""
    if choice not in word:
        lives -= 1

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
    elif lives == 0:
        game_over = True
        print(stages[lives])
        print("YOU LOSE")