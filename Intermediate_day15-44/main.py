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
#variables
run_machine = True
drink = ""
#functions

def check_drink():
    drink = ""
    while drink not in MENU:
        drink = input(f"What would you like? (espresso/latte/cappuccino):").lower()
        if drink == "off":
            print(f"Turning of machine.")
            run_machine = False
            return drink
        #elif drink not in MENU:
            #print(f"{drink} is not on the Menu\nPlease Enter a drink on the menu.")
        #else:
            #return drink

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while run_machine == True:
    check_drink()
    if drink == "off"
        print("Broken")