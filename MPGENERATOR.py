import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a random mix of all character sets
    if length > 4:
        all_characters = lowercase + uppercase + digits + special_characters
        password += random.choices(all_characters, k=length-4)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length and number of passwords
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 4:
                print("Password length should be at least 4 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords < 1:
                print("Number of passwords should be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate and display the passwords
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i + 1}: {password}")

if __name__ == "__main__":
    main()
