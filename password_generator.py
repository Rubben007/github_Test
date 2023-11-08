import random
import secrets
import string


def generat_password(length=12, use_uppercase=True, use_lowercase=True, use_specials=True, use_digit=True):
    character = string.ascii_letters if use_uppercase else string.ascii_lowercase
    if use_digit:
        character += string.digits
    if use_specials:
        character += string.punctuation
    
    password = "".join(secrets.choice(character) for _ in range(length))
    return password
