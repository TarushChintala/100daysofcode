MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(drink):
    for items in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True

def payment(drink):
    print("Please insert coins")
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))
    paid = 0.25 * quarters + 0.1 * dimes + 0.05 *  nickels + 0.01 * pennies
    if MENU[drink]["cost"] > paid:
        print("Sorry that is not enough money")
        return False
    else:
        change = paid - MENU[drink]["cost"]
        print(f"Here is ${round(change,2)} in change")
        return True

def deduct_resources(drink):
    for items in MENU[drink]["ingredients"]:
        resources[items] -= MENU[drink]["ingredients"][items]


money  = 0
power = True
while power:

    user_input = input("\n\n\nWhat would you like? (espresso, latte, cappuccino) ").lower()

    if user_input == "off":
        power = False

    if user_input == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}ml")
        print(f"Money : ${money}")

    if user_input == "espresso":
        if check_resources("espresso"):
            if payment("espresso"):
                money += MENU["espresso"]["cost"]
                deduct_resources("espresso")

    if user_input == "latte":
        if check_resources("latte"):
            if payment("latte"):
                money += MENU["latte"]["cost"]
                deduct_resources("latte")

    if user_input == "cappuccino":
        if check_resources("cappuccino"):
            if payment("cappuccino"):
                money += MENU["cappuccino"]["cost"]
                deduct_resources("cappuccino")