def greet():
    print("Hey there!")
    print("How are you")
    print("It has been a while")
greet()

name = input("What is your name?")

def greet_with_name(name):
    print(f"Hello there,{name}")
    print(f"{name},when was the last time we met?")

greet_with_name(name)