from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
        objects = menu.get_items()
        choice = input(f"Select your drink from our Menu: {objects}\n")
        if choice == "report":
            print(money_machine.report())
            print(coffee_maker.report())
        elif choice == "off":
            is_on = False
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        
