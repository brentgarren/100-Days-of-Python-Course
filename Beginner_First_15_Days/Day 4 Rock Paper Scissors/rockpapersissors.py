import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = True
keep_playing = True
options = [rock,paper,scissors]

choice = 5
computer_choice = ""    
while game == True:
    choice = int(input(f"Select 0 for rock\n1 for paper\n2 for scissors?\n"))
        
    print(f"You chose \n{options[choice]}")
    computer_choice = random.randint(0,2)
    print(f"Computer chose {options[computer_choice]}")

    if choice == computer_choice:
        print(f"The game is a draw!")
    elif choice == 0 and computer_choice == 1:
        print(f"You lose!")
    elif choice == 0 and computer_choice == 2:
        print("You Win!")
    elif choice == 1 and computer_choice == 2:
        print(f"You lose!")
    elif choice == 1 and computer_choice == 0:
        print("You Win!")
    elif choice == 2 and computer_choice == 0:
        print(f"You lose!")
    elif choice == 2 and computer_choice == 1:
        print("You Win!")
    else:
        print(f"Invalid Option!")
    while keep_playing == True:
        choice = str(input(f"Do you want to continue Y/N?\n"))
        if choice.lower() == "n":
            sys.exit()
        elif choice.lower() == "y":
            print(f"The game continues!")
            break
        else:
            print(f"Invalid Selection")  
