import random

logo = '''
   ___                  _   _          _  _            _             
  / __|_  _ ___ ______ | |_| |_  ___  | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-< |  _| ' \/ -_) | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/  \__|_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|  
                                                                     
'''
attempts = 0
game_over = False
difficulty_select = False
correct_number = random.randint(1,100)
guess = ""

DIFFICULTY_HARD = 5
DIFFICULTY_EASY = 10


def gameplay(difficulty):
    if difficulty == 'easy':
        return DIFFICULTY_EASY
    if difficulty == 'hard':
        return DIFFICULTY_HARD
    return 0

print(logo)

print(f"Welcome to the Number Guesssing Game!\nI'm thinking of a number between 1 and 100.")
while difficulty_select == False:
    difficulty = str(input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower())
    attempts = gameplay(difficulty)
    if attempts > 0:
        break
while game_over == False:
    guess = int(input(f"Guess a number between 1 and 100!: "))
    if guess == correct_number:
        print("You Win")
        break
    elif guess > correct_number:
        print('To High!')
        attempts -= 1
        print(f"You have {attempts} remaining!")
    elif guess < correct_number:
        print(F'Too low!')
        attempts -= 1
        print(f"You have {attempts} remaining!")
    else:
        print("enter a valid number!")
    if attempts == 0:
        print(f"You lose the correct number was {correct_number}")    
        break
