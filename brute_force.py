"""Brute Force Password Cracker"""
import itertools
import string
import time


def common_guess(word: str) -> str:
    """checks a list of common password """
    with open('passwords.txt', 'r', encoding="utf-8") as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'


def brute_force(word: str, length: int, digits:
                bool = False, symbols: bool = False) -> str:
    """brute force password cracker"""
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses'

        # print(guess, attempts)


def main():
    """Main function and progran entry point"""
    print('Searching .....')
    password: str = 'craig'
    my_len = len(password)

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=my_len,
                                  digits=True, symbols=False):
            print(cracked)
        else:
            print('There was no match')
    end_time: float = time.perf_counter()

    print(round(end_time - start_time, 2), 's')


if __name__ == '__main__':
    main()
