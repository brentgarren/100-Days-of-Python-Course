import platform
import os
logo = '''
    ________                 __  __   _      
   / ____/ ____  _________ _/ /_/ /_ ( )_____
  / __/ / /_  / / ___/ __ `/ __/ __ \|// ___/
 / /___/ / / /_/ /  / /_/ / /_/ / / / (__  ) 
/_____/_/ /___/_/   \__,_/\__/_/ /_/ /____/  
                                                                                  
'''
name1 = '''
   ______                              _______       __             
  / ________ ____  _________ ______   / ____(_____  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  / /_/ / /     / /___/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/      \____/_/ .___/_/ /_/\___/_/     
                                          /_/                       
'''
alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')

def get_message():
    output = str(input("Message: ")).replace(" ", "")

    return output
def get_shift():
    shift = int(input("Type the shift number:\n"))
    clear_console()
    return shift


def encrypt(text):
    shift_allowed = False
    while shift_allowed == False:  
        shift = get_shift()
        if shift >= 0 and shift <= 25:
            shift_allowed = True
    encrypted_message = ""
    for char in text.lower():
        indexnum = alphabet.index(char)
        indexnum = indexnum + shift
        if indexnum >= 25:
            indexnum -= 25
        encrypted_message += alphabet[(indexnum)]
    print(encrypted_message)    
    return encrypted_message
        
def decrypt(text, brute_shift, direction=0):
    shift_allowed = True
    direction = str(direction)
    decrypted_message = ""
    if direction == "decode" or direction == "2":
        shift_allowed = False
    if not brute_shift:
        while shift_allowed == False:  
            brute_shift = get_shift()
            if brute_shift >= 0 and brute_shift <= 25:
                shift_allowed = True

    for char in text:
        indexnum = int((alphabet.index(char)-brute_shift))
        if indexnum < 0:
            indexnum = indexnum + 25
        decrypted_message += alphabet[indexnum]

    print(f"{brute_shift} {decrypted_message}")

def bruteforce(text, direction):
    brute_shift = 0

    for num in range(1,26):
        brute_shift += 1
        decrypt(text, brute_shift, direction)

###### Caeser Cipher ######

# Look up match case statements

while True:
    clear_console()
    print(f"{logo}{name1}")
    direction = str(input("Please select a Mode:\n1. Encode\n2. Decode\n3. Bruteforce\n\nMode: ")).lower()
     

    if direction == "encode" or direction == "1":
        clear_console()   
        encrypt(get_message())
        break
    elif direction == "decode" or direction == "2":
        clear_console()   
        decrypt(get_message(), False, direction)
        break
    elif direction == "bruteforce" or direction == "3":
        clear_console()   
        bruteforce(get_message(), direction)
        break
    else: 
        print(f"Incorrect option!")
