import platform
import os

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')

def get_message():
    output = str(input("Message: "))
    clear_console()
    return output
def get_shift():
    shift = int(input("Type the shift number:\n"))
    clear_console()
    return shift


def encrypt(text):
    shift_allowed = False
    while shift_allowed == False:  
        shift = get_shift()
        if shift >= 0 and shift <= 26:
            shift_allowed = True
    encrypted_message = ""
    for char in text.lower():
        indexnum = alphabet.index(char)
        indexnum = indexnum + shift
        if indexnum >= 26:
            indexnum -= 26
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
            if brute_shift >= 0 and brute_shift <= 26:
                shift_allowed = True

    for char in text:
        indexnum = int((alphabet.index(char)-brute_shift))
        if indexnum < 0:
            indexnum = indexnum + 26
        decrypted_message += alphabet[indexnum]

    print(f"{brute_shift} {decrypted_message}")

def bruteforce(text, direction):
    brute_shift = 0

    for num in range(1,27):
        brute_shift += 1
        decrypt(text, brute_shift, direction)

###### Caeser Cipher ######

# Look up match case statements

while True:
    clear_console()
    direction = str(input("Please select a mode:\n1. Encode\n2. Decode\n3. Bruteforce\n".lower()))
    clear_console()    

    if direction == "encode" or direction == "1":
        encrypt(get_message())
        break
    elif direction == "decode" or direction == "2":
        decrypt(get_message(), False, direction)
        break
    elif direction == "bruteforce" or direction == "3":
        bruteforce(get_message(), direction)
        break
    else: 
        print(f"Incorrect option!")
