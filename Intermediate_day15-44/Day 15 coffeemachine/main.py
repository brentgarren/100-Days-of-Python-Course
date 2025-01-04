import os
import platform
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

#variables
run_machine = True
drink = ""

#functions
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else: 
        os.system('clear')

def what_drink():
    drink = ""
    options = "/".join(MENU.keys())
    while drink not in MENU:
        drink = input(f"What would you like? ({options}): ").lower()
        if drink == "off":
            print("Turning off machine...")
            time.sleep(5)
            return drink  # Return "off" to signal the machine should stop
        if drink == "report":
            print("Running report...")
            time.sleep(5)
            return drink  # Return "report" to signal the machine should start running a report
        if drink in MENU:
            break
        else:
            print(f"{drink} is not on the menu.\nPlease enter a drink on the menu.")
            time.sleep(3)
            clear_console()
    return drink  # Returns the selected drink


def check_drink(drink):
    clear_console()
    if drink == "off":
        return False
    elif drink == "report":
        for resource, amount in resources.items():
            if resource == "water":
                print(f"{resource.capitalize()}: {amount}ml")
            elif resource == "milk":
                print(f"{resource.capitalize()}: {amount}ml")
            elif resource == "coffee":
                print(f"{resource.capitalize()}: {amount}g")
            elif resource == "money":
                print(f"{resource}: ${amount:.2f}")
        return False
    else:
        return True

def check_resources(drink):
    for ingredient, required_amount in MENU[drink]["ingredients"].items():
        if required_amount > resources.get(ingredient, 0):
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        return True

def make_drink(drink):
    for ingredient, required_amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= required_amount
     
def pay_for_drink(drink):
    cost = MENU[drink]["cost"]
    original_cost = MENU[drink]["cost"]
    print(f"Your drink costs ${cost}")
    while cost > 0:
        try:
            quarters = int(input(f"Insert Quarters: "))
            cost -= (quarters * .25)
        except ValueError:
            print(f"Invalid input. Please enter a valid number of coins.") 

        try:
            dimes = int(input(f"Insert Dimes: "))
            cost -= (dimes * .10)
        except ValueError:
            print(f"Invalid input. Please enter a valid number of coins.")

        try:    
            nickels = int(input(f"Insert Nickels: "))
            cost -= (nickels * .05)
        except ValueError:
            print(f"Invalid input. Please enter a valid number of coins.")

        try:    
            pennies = int(input(f"Insert Pennies: "))
            cost -= (pennies * .01)
        except ValueError:
            print(f"Invalid input. Please enter a valid number of coins.")        

            if cost > 0:
                print(f"You still owe {cost:.2f}")
                try:
                    cancel = str(input(f"Cancel Order?: Y / N:\n"))
                    if cancel.lower() == "y":
                        clear_console()
                        break
                except ValueError:
                    print(f"Invalid input. Please enter a valid selection.") 
        resources["money"] += original_cost
        clear_console()
        make_drink(drink)
        print(f"Your change is ${abs(cost):.2f}")
        print(f"Your {drink} is now ready!")
        break


#<----Program starts here ---->
while run_machine:
    drink = what_drink()
    if drink == "off":
        run_machine = False
    if check_drink(drink):
        if not check_resources(drink):
            print(f"You cannot make this drink.")
        else:
            pay_for_drink(drink)
            time.sleep(10)


                      
            


    