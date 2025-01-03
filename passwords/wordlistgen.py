import itertools
import random

# Define character sets
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
all_chars = vowels + consonants

# Function to check if a password meets the requirements
def is_valid(password):
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = sum(1 for char in password if char in consonants)
    return len(password) >= 6 and vowel_count >= 2 and consonant_count >= 1

# Generate passwords
passwords = set()
for length in range(6, 9):  # Set the maximum length (e.g., 8 for demo purposes)
    for pwd_tuple in itertools.product(all_chars, repeat=length):
        password = ''.join(pwd_tuple)
        if is_valid(password):
            passwords.add(password)

# Save the valid passwords to a file
with open("custom_wordlist.txt", "w") as f:
    for password in passwords:
        f.write(password + "\n")

print("Generated wordlist saved as custom_wordlist.txt")
