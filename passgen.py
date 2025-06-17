#!/usr/bin/env python3

import secrets
import string
import pyperclip
import time

def generate_password(length=12):
    
# Define characters to use
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

try:
    user_length = int(input("Enter password length (default 12): ") or 12) # Ask user for desired lenght
    password = generate_password(user_length)
    print("Generated password:", password)

    copy_choice = input("Copy to clipboard? (Y/n)").strip().lower() # Ask user if they want to copy to system clipboard

    if copy_choice in  ["", "y", "yes"]:
        pyperclip.copy(password)
        print("Password copied to clipboard for 10 seconds...")
        time.sleep(10)
        pyperclip.copy("")
        print("Clipboard cleared.") #Clear the clipboard
    else:
        print("Password was not copied.")

except ValueError:
    print("Please enter a valid number.") # If no number is typed in
