from game_data import data
from art import *
import random
import os
import platform

def select_person():
    return random.choice(data)
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else: 
        os.system('clear')  

def verse(player,option):
      global follower_count
      name = player['name']
      follower_count = player['follower_count']
      description = player['description']
      country = player['country']
      print(f"Compare {option}: {name}, {description}, from {country}.")

def game():
    game_over = False
    was_right = False
    score = 0
    
    clear_console()

    while game_over == False:
        print(logo)
        if score > 0:
            print(f"You're right! Currnet score: {score}.")

        if was_right == False:
            player = select_person()

        verse(player, 'A')
        player1_score = follower_count
        print(vs)
        verse(select_person(), 'B')
        player2_score = follower_count

        while True:
            choice = str(input(f"Who has more followers? Type 'A' or 'B': ")).lower()

            if choice == 'a':
                if player1_score > player2_score:
                    clear_console()
                    score += 1
                    was_right = True
                else:
                    print(f'Sorry, that\'s wrong. Final score: {score}')
                    was_right = False
                    game_over = True
                break
            elif choice == 'b':
                if player2_score > player1_score:
                    clear_console()
                    score += 1
                    was_right = True
                else:
                    print(f'Sorry, that\'s wrong. Final score: {score}')
                    was_right = False
                    game_over = True
                    break
            else:
                print(f"Select a Valid Response!")



game()