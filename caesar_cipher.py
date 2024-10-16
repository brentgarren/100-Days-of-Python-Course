alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

indexnum = ""
is_true = False
shift_allowed = True

def encrypt():
    text = input("type your message here:\n".lower())
    shift_allowed = False
    while shift_allowed == False:  
        shift = int(input("Type the shift number:\n"))
        if shift >= 0 and shift <= 26:
            shift_allowed = True
    encrypted_message = ""
    for char in text.lower():
        indexnum = alphabet.index(char)
        if indexnum >= 26:
            indexnum = indexnum - 26
        encrypted_message += alphabet[(indexnum+shift)]
    print(encrypted_message)    
        
def decrypt():
    decrypted_message = ""
    text = input("type your message here:\n".lower())
    if direction == "decode" or direction == "2":
        global shift_allowed
        shift_allowed = False
    if shift_allowed == False:
        while shift_allowed == False:  
            shift = int(input("Type the shift number:\n"))
            if shift >= 0 and shift <= 26:
                shift_allowed = True
    shift = int(input("Type the shift number:\n"))
    for char in text:
        indexnum = int((alphabet.index(char)-shift))
        if indexnum <= 0:
            indexnum = indexnum + 26
        decrypted_message += alphabet[indexnum]
    print(decrypted_message)

def bruteforce():
    shift = 0
    for num in range(1,25):
        shift +=1
        decrypt()

###### Caeser Cipher ######

while is_true == False:
    direction = input("Please select a mode:\n1. Encode\n2. Decode\n3. Bruteforce\n".lower())
    if direction == "encode" or direction == "1":
        encrypt()
        is_true = True
    elif direction == "decode" or direction == "2":
        decrypt()
        is_true = True
    elif direction == "bruteforce" or direction == "3":
        bruteforce()
    else: 
        print(f"Incorrect option!")
