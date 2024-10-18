import platform
import os

def get_name():
    return str(input(f"Welcome to the secret auction program.\nWhat is your name?: "))

def get_bid():
    return int(input("what's your bid?: $"))

def more_bidders():
    more_bids = str(input(f"Are there any other bidders? Type 'yes' or 'no'. "))
    if more_bids == "yes":
        return True
    else:
        return False

def add_bid(name, bid):
    list_of_bids[name] = bid

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')

list_of_bids = {}
max_bidder = "No Bidder"
max_bid = 0

while True:
    name = get_name()
    bid = get_bid()
    add_bid(name, bid)
    clear_console()
    if not more_bidders():
        break

for name in list_of_bids:
    if list_of_bids[name] > max_bid:
        max_bidder = name
print(f"The winner is {max_bidder} with a bid of ${list_of_bids[max_bidder]}.")


    
