import random
import string


def generate_passwords(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        print("Error: Select at least one character type to generate a password")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the password generator!")
    length = int(input("What password length do you need? "))
    use_uppercase = input("Do I include upper case letters? (yes/no) ").lower() == 'yes'
    use_lowercase = input("Do I include lower case letters? (yes/no) ").lower() == 'yes'
    use_digits = input("Should the numbers be included? (yes/no) ").lower() == 'yes'
    use_special_chars = input("Do I include special characters? (yes/no) ").lower() == 'yes'

    password = generate_passwords(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    if password:
        print("Your generated password:", password)

if __name__ == "__main__":
    main()