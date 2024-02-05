import random
import string

def generate_password(length):
    # Define character sets for different complexities
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based  on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8  characters
    length = max(length, 8)

    # Generating the password using random.choices
    password = ''.join(random.choices(all_characters, k=length))

    return password

def main():
    # Gets the  user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generateing  and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
