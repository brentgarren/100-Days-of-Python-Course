
import os
import platform
import time
import sys
import random

##Functions##
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else: 
        os.system('clear')
def loading():
    num_stars = 0
    while num_stars < 3:
        print("*")
        time.sleep(1)
        num_stars += 1
    num_stars = 0
    clear_console()
def treasure_map():
    print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
      ''')
def start_game():
    start = ""
    while start.lower() != "start":
        start = str(input("Type start when ready to begin! "))
def death():
    print('''
                   88                               88           
         88                         ,d    88           
         88                         88    88           
 ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
8b       88 8PP""""""" ,adPPPPP88   88    88       88  
"8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
 `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88 
          ''')
    time.sleep(10)
    sys.exit()
def monster():
    print(f'''
                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\           )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
   -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\\
    -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \\
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \\
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```       
''')
def treasure():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/
          ''')
def heart():
    print('''
 ,-.-.
 `. ,'
   `
    ''')
##Game
xtra_luck = 0
dum_luck = 0

#Introduction
treasure_map()
print("Welcome to the Island of Lost Ones")
print("Your mission is to find the lost treasure")
start_game()
print("You begin your adventure by setting off towards the forest")
loading()
print("The entrance to a cave lies before you, a dark maw that seems to swallow all light. Armed with only a torch and your wits, you step inside.")
choice = ""
while choice != "1" and choice != "2":
    print(f"1. Enter cave carefully.\n2. Rush in without hesitation. ")
    choice = str(input(f"Make your decision: "))
if choice != "1":
    loading()
    dum_luck += 1
    skill_check = random.randint(0, 10)
    if skill_check % 2 == 0:
        print("Game Over: You trip over loose stones and fall into a hidden pit, meeting an untimely end.")
        death()
    else:
        print(f"While its never the smartest idea to rush in blindly, this time it works out!")
        if skill_check >= 5:
            xtra_luck += 1
loading()

# The First Fork
choice = ""
print(f"As you cautiously move deeper into the cave, you come to a fork in the path. One tunnel seems narrow but smooth, while the other is wide yet covered in strange, glowing moss.")
while choice != "1" and choice != "2":
    print(f"1. Take the narrow path.\n2. Take the moss-covered path. ")
    choice = str(input(f"Make your decision: "))
if choice != "2":
    print("Game Over: The narrow tunnel suddenly collapses behind you, trapping you inside with no way to turn back.")
    death()
loading()
# The Mossy Tunnel
choice = ""
print(f"You choose the moss-covered path, and after a short distance, you feel the temperature drop sharply. Ahead, you see an underground river, fast and icy cold, blocking your way.")
while choice != "1" and choice != "2":
    print(f"1. Swim across the river.\n2. Look for another way around. ")
    choice = str(input(f"Make your decision: "))
while choice == 2:
    print("You waste time circling the river and eventually end up back where you started, losing precious hours.")
    print(f"1. Swim across the river.\n2. Look for another way around. ")
    choice = str(input(f"Make your decision: "))
loading()
print(f"You dive into the icy waters. It's freezing, but you manage to cross safely to the other side.")

# Echoing Chamber
choice = ""

print(f"You arrive at a vast cavern with high ceilings. Strange echoes bounce off the walls, disorienting you. Suddenly, you hear movement from the creatures that dwell in the cave are drawing near.")
while choice != "1" and choice != "2":
    print(f"1. Hide behind a boulder and wait for the creatures to pass.\n2. Run deeper into the cavern to escape. ")
    choice = str(input(f"Make your decision: "))
if choice != "1":
    loading()
    monster()
    print("Game Over: The narrow tunnel suddenly collapses behind you, trapping you inside with no way to turn back.")
    death()
loading()
print(f"You hide behind the boulder, and after a tense moment, the creatures pass without noticing you. As you emerge, you spot a narrow hidden passage in the far corner of the cavern.")
time.sleep(3)


# The Hidden Passage
choice = ""

while choice != "1" and choice != "2":
    print(f"1.  Enter the hidden passage.\n2. Ignore the passage and stay on the main path. ")
    choice = str(input(f"Make your decision: "))
if choice == "1":
    loading()
if choice == "2":
    loading()
    luck = 0
    randomnum = random.randint(1,10)
    while randomnum != luck:
        print("The main path leads you in circles, disorienting you until you're hopelessly lost.")
        print(f"1. Continue to find a way out. 2. Give up?")
        choice = str(input(f"Make your decision: "))
        if choice == "2":
            death()
        luck = random.randint(1,10-xtra_luck)
        randomnum = random.randint(1,10-xtra_luck)
        loading()
        if luck == 10 and randomnum == 10:
            print(f'You find yourself in vast room filled with treasure')
            time.sleep(2)
            treasure()
            print(f'You gather up as much treasure as you can carry, then begin to leave back the way you came')
            xtra_luck += 2
        if luck == 1 and randomnum == 1:
            print(f"Your luck eventually runs out while wandering aimlessly in the darkness")
            clear_console()
            time.sleep(5)
            monster()
            time.sleep(5)
            death()
    loading()
#The Puzzle Room
choice = ""
loading()
print(f"The hidden passage leads to a small room filled with ancient carvings and strange symbols. In the center of the room is a pedestal with a glowing gem that seems important. However, there are also several stone tiles on the floor that look like a trap.")
while choice != "1" and choice != "2":
    print(f"1. Step on the stone tiles and approach the gem.\n2. Look around the room for clues to disable the trap. ")
    choice = str(input(f"Make your decision: "))
if choice != "2":
    loading()
    print("Game Over: The tiles trigger a deadly trap, and the ceiling collapses, burying you beneath the rubble.")
    death()
print(f"You examine the carvings closely and discover a sequence of symbols that correspond to the safe tiles. Carefully stepping on the correct tiles, you reach the gem. When you take it, a hidden door opens, leading deeper into the cave.")

## The bridge
choice = ""
loading()
print(f"The door leads to a massive underground chasm. The only way across is a narrow stone bridge that looks fragile. Below, you hear the sound of rushing water and feel a gust of wind from the depths.")
while choice != "1" and choice != "2":
    print(f"1. Cross the stone bridge slowly and carefully.\n2. Run across quickly before it collapses. ")
    choice = str(input(f"Make your decision: "))

distance = 10
print(f'''
 O
/|\ [][][][][][][][][][][]
/\   /\   /\   /\   /\  /\\
''')
luck = random.randint(1,10) + xtra_luck
if choice == "1":
    luck += 2
    while distance > 0:
        luck -= 1
        if luck <= 0:
            print("The bridge gives out to your weight and you fall.")
            death()
        distance -= 2
        print(f" You carefully make your way closer to the otherside")
        print("[]" * (distance + 2))
        time.sleep(2)
        if luck <= 2:
            dum_luck += 1
if choice == "2":
    luck -= 1
    while distance > 0:
        luck -= random.randint(1,2)
        if luck <= 0:
            print("The bridge gives out to your weight and you fall.")
            death()
        distance -= 4
        print("You continue running across the bridge.")
        print("[]" * (distance + 2))
        xtra_luck += 1
        if luck <= 2:
            dum_luck += 2
        time.sleep(2)
loading()
print("You cross the bridge carefully and arrive at the final chamber. At the center lies the Heart of the Abyss, pulsing with dark energy. However, standing between you and the artifact is a guardian made of stone, its eyes glowing with ancient power.")
guardian_health = 25 - xtra_luck - dum_luck
player_health = 10 + xtra_luck + dum_luck
monster()
time.sleep(4)
choice = 0
round_timer = 1
while guardian_health > 0:
    if player_health <= 0:
        print(f"You died fighting the monster")
        print(f"Guardian Health: {guardian_health}\n\n\n\n\n\n")
        time.sleep(10)
        death()
    clear_console()
    print('''
 ,-.-.
 `. ,'
   `
          ''')          
    print(f"Player Health: {player_health}")
    print(f"Round: {round_timer}")
    choice = 0
    if xtra_luck > 3:
        xtra_luck -= 2
        print(f"You feel as if you've spent all of your luck")
    if xtra_luck < -3:
        xtra_luck += 6
        print(f'The entity in the heart of the abyss watches over you.')
    if round_timer > 4:
        print(f'Proximity to the heart has made you feel luckier')
        xtra_luck +=1
    print(f"1. Attack!\n2. Dodge! ")
    choice = str(input(f"Make your decision: "))
    monster_roll = random.randint(0,11)
    print(f"Monster Rolled: {monster_roll}")
    if choice == "2":
        monster_roll -= 1
    if choice == "1":
        luck = (0 + xtra_luck)
        randomnum = random.randint(1,10)
        luck += (randomnum - 2)
        if luck >= 6:
            guardian_health -= 1
            if luck >= 8:
                guardian_health -= 2
                print(f"Feeling Lucky")
                xtra_luck += 1
                time.sleep(2)
        if luck <= 3:
            player_health -= 1
            if luck <= 1:
                player_health -= 2
                xtra_luck -= 1
                print(f"You have a feeling of dread take over you.")
                time.sleep(2)
    monster_roll = random.randint(0,11)
    monster_ability = monster_roll % 2
    if choice == "2":
        monster_roll -= 2
    if monster_roll > 8:
        player_health -= 1
        if monster_roll >= 10:
            player_health -= 1
    if monster_roll <= 4:
        player_health += 1
        if monster_roll <= 2:
            player_health += 1
            print(f'You feel healthier!')

    if monster_ability == 0:
        print(f'The monster readies an attack')
        if choice == 1:
            player_health -= 2
            print(f"The monster takes advantage of an opening in your attack")
            if (monster_roll - xtra_luck) > 5:
                print(f"The monster grabs you by the neck and slams you to the ground")
                player_health -= 1
                xtra_luck -= 2
                print(f"You aren't sure how this will affect you going forward")
                time.sleep(2)
                if monster_roll >= 7:
                    player_health -= 2
                    guardian_health += 1
                    time.sleep(2)
            if (monster_roll - xtra_luck) <= 5:
                print(f"The monster swipes at you but your agility causes the monster to graze you")
                player_health += 1
                if monster_roll <= 2:
                    player_health += 1
                    print(f"Feeling Lucky")
                    xtra_luck += 1
                    print(f'You are able take advantage of the missed attack to counterattack!')
                    guardian_health -= 2
                    time.sleep(2)
    if monster_ability == 1:
        print(f"You caught the monster offguard with your attack!")
        guardian_health -= 2
        if (monster_roll - xtra_luck) <= 4:
            guardian_health -= 1
            time.sleep(2)
            if monster_roll <= 2:
                print(f'You strike a critical point!')
                print(f"Feeling Lucky")
                xtra_luck += 1
                guardian_health -= 4
                time.sleep(2)
        if monster_roll - xtra_luck >= 5:
            guardian_health += 1
            player_health -= 1
            time.sleep(2)
        if monster_roll >= 9:
            print(f'You missed your attack, angering the monster further!')
            xtra_luck -= 3
            guardian_health += 2
            time.sleep(2)
    round_timer += 1
print(f'The Monster is Felled!')
time.sleep(5)
loading()
print(f"With the guardian defeated, you approach the Heart of the Abyss. As you reach out to claim it, a final choice looms before you. The artifact whispers to you, offering you immense power, but at a great cost.")
choice =""
while choice.lower() != "y" or choice.lower() != "n": 
    choice = str(input(f"Do you accept it? Yes or No: "))
    if choice.lower() == "yes":
        print(f"You claim the Heart, and immense power floods your body. However, its dark energy corrupts you, transforming you into a vessel for the ancient evil that once ruled the world.")
        monster()
        print(f'You Win?')
    else:
        print(f"You walk away, knowing that no power is worth the cost of your soul. You escape the cave, having resisted the temptation, and return to the surface.")
        print(f"You Win!")
