# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

restart = True
bidders = {}
max = 0
buyer = ""

while restart:
    name = input("Enter your name:")
    bid = int(input("Enter your bid:"))
    bidders[name] = bid
    proceed = input("Are there more bidders?").lower()
    if proceed == "no":
        restart = False
    print("\n"*20)

for i in bidders:
    if bidders[i] > max:
        buyer = i
        max = bidders[i]

print("\n"*20)
print(logo)
print(f"The item is sold to {buyer} with a bid of {max}")