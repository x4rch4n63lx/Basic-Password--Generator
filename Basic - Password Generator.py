import random
import string

# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 1/22/2025 - 12:32 AM
# Script Purpose : Basic - Password Generator
# Description    : This script generates a random password based on user-defined criteria.
#                                                  
# 
# Features       : - Generate a random password
#                  - Option to exclude certain characters
#                  - Password strength check
#                  
#                  
# Usage Note     : Run the script and follow the prompts to generate a secure password.
# ===================================================================================

def generate_password(length, exclude_chars=None):
    characters = string.ascii_letters + string.digits + string.punctuation
    if exclude_chars:
        characters = ''.join([c for c in characters if c not in exclude_chars])
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_punctuation = any(c in string.punctuation for c in password)
    return len(password) >= 8 and has_upper and has_lower and has_digit and has_punctuation

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            exclude_chars = input("Enter any characters you want to exclude (leave blank if none): ")
            password = generate_password(length, exclude_chars)
            if not check_password_strength(password):
                print("Generated password is not strong enough. Generating another...")
                continue
            print(f"Your new password is: {password}")
            input("Press Enter to exit...")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
