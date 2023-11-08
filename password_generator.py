import random
import secrets
import string



def generate_password(length=8, use_uppercase=True, use_lowercase=True, use_specials=True, use_digit=True):
    combination = string.ascii_letters if use_uppercase else string.ascii_lowercase
    if use_digit:
        combination += string.digits
    if use_specials:
        combination += string.punctuation
    
    password = "".join(secrets.choice(combination) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("enter password_length: "))
        use_uppercase = input("use_uppercase? (y/n): ").lower() == "y"
        use_lowercase = input("use_lowercase? (y/n): ").lower() == "y"
        use_digit = input("use_digit? (y/n): ").lower() == "y"
        use_specials = input("use_specials? (y/n): ").lower() == "y"
        
        generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_digit, use_specials)
        print(f"Generated_password", {generated_password})
    except ValueError:
        print("enter a valid password length")

if __name__ == "__main__":
    try:
        password_length = int(input("enter password_length: "))
        use_uppercase = input("use_uppercase? (y/n): ").lower() == "y"
        use_lowercase = input("use_lowercase? (y/n): ").lower() == "y"
        use_digit = input("use_digit? (y/n): ").lower() == "y"
        use_specials = input("use_specials? (y/n): ").lower() == "y"
        
        generated_password = generat_password(password_length, use_uppercase, use_lowercase, use_digit, use_specials)
        print(f"Generated_password", generated_password)
    except ValueError:
        print("enter a valid password length")
