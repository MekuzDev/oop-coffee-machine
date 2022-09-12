import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()

is_on = True

while is_on:
    choice = input(f'what would you like ? {menu.get_items()}: ').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        payment.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if payment.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
