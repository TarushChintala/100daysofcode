print("Welcome to the tip calculator")
bill = float(input("What was the total bill?: $\n"))
tip_p = float(input("How much tip would you like to pay? 10, 12 or 15?:-\n"))
ppl = float(input("How many people is it split between?:-\n"))
split = (tip_p / 100 * bill + bill) / ppl
split = round(split, 2)
print(f"Each person should pay:- ${split}")