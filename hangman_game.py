import random
import os
import platform


#Functions
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else: 
        os.system('clear')
def list_letters(letters):
    global lives
    global choice
    if letters not in guessed_letters:
        guessed_letters.append(letters)
        choice = True
        if letters not in correct_word:
            lives -= 1
    else:
        print(f"You've already guessed that letter!")
            


#Lists
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ['aardvark', 'baboon', 'camel']
guessed_letters = []
correct_letters = []

#Variables
HANGMAN.reverse()
game_over = False
correct_word = random.choice(word_list)
placeholder = ""
length_of_Word = len(correct_word)
lives = 6
display = ""
guess = ""

clear_console()
#Get Length of Correct Word
for space in range(length_of_Word):
    placeholder += "_"


#Hangman Game
while game_over == False:

    if lives == 6:
        print(HANGMAN[lives])
        print(placeholder)
        print(guessed_letters)
    else:
        print(HANGMAN[lives])
        print(display)
        print(guessed_letters)
    choice = False
    while choice == False:
        guess = str(input("Guess a Letter: ").lower())
        list_letters(guess)
    display = ""
    
    for letter in correct_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if "_" not in display:
        clear_console()
        print(HANGMAN[lives])
        print(guessed_letters)
        game_over = True
        print(f"You win!")

    if lives == 0:
        clear_console()
        print(HANGMAN[lives])
        print(guessed_letters)
        game_over = True
        print(f"You lose!")
        print(f"The correct word was: {correct_word}")  
    clear_console()
