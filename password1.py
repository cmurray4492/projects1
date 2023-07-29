"""Random Password Generator"""
import string
import secrets


def contains_upper(password: str) -> bool:
    '''does the password contain an upper case character'''
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    '''does the password contain a symbol'''
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    '''function to generate a random password'''
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_password(
            length=30, symbols=True, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f"{i} -> {new_pass} ({specs})")
