import random
word_list = ["aardvark","camel","baboon"]

word = random.choice(word_list)

placeholder = ""

for i in word:
    placeholder += "_"
print(placeholder)

choice = input("Guess a letter:\n").lower()

display = ""

for letter in word:
    if choice == letter:
        display += letter 
    else:
        display += "_"

print(display)