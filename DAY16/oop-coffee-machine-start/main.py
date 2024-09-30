from mimetypes import inited

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power = True
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while power:
    user_input = input("\n\nWhat would you like? (espresso, latte, cappuccino): ").lower()
    if user_input == "report":
        coffee.report()

    elif user_input == "off":
        power = False

    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee.is_resource_sufficient(drink):
                paid = money.make_payment(drink.cost)
                if paid:
                    coffee.make_coffee(drink)