import random
word_list = ["aardvark","camel","baboon"]

word = random.choice(word_list)

letter = input("Guess a letter:\n").lower()

for i in word:
    if letter == i:
        print("Right")
    else:
        print("Wrong")