import random
import os
import platform

game = ""
player_score = 0
computer_score = 0
players_cards = []
computer_cards = []
cards_in_play = []
play_game = 'Y'

cards = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    'A' : 11,
}

list_of_cards = list(cards.keys())
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else: 
        os.system('clear')

def deal_card():
    good_card = False
    while not good_card:
        card = random.choice(list_of_cards)
        cardcount_in_play = cards_in_play.count(card)
        if cardcount_in_play < 4:
            cards_in_play.append(card)
            good_card = True
            return card
            





#start of game

for _ in range(2):
    players_cards.append(deal_card())
    computer_cards.append(deal_card())

while player_score <= 21:
    player_score = 0
    for card in players_cards:
        player_score += cards[card]   
    if player_score > 21:
        if 'A' in players_cards:
            count_A = players_cards.count('A')
            for _ in range(count_A):
                if player_score > 21:
                    player_score = (player_score - 10)
        if player_score > 21:
            clear_console()
            print(players_cards)
            print(player_score)
            print('Bust')
            break
    for card in computer_cards:
        computer_score += cards[card] 
    if computer_score < 17:
        computer_cards.append(deal_card())
        print(f"Computer's Cards: {computer_cards[2:]}")
    elif computer_score > 21:
        print(f"Computer has Busted!")
    else:
        print(f"Computer has Stood!")

    print(f"Your Cards: {players_cards}")
    print(f'Player Score: {player_score}')
    hit = str(input(f" Hit? 'Y' 'N'\n")).lower()
    if hit == 'y':
        players_cards.append(deal_card())
        clear_console()
    else:
        break
if player_score > computer_score:
    print(f"You win!")
elif computer_score > 21:
    print(f"You Win!")
else:
    print('You lose!')
