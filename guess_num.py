"""Number guessing game"""
from random import randint
from colorama import Fore, init

lower_num, higher_num = 1, 100

random_number: int = randint(lower_num, higher_num)
print(Fore.LIGHTCYAN_EX +
      f"Guess the number in the range from {lower_num} to {higher_num}.")

while True:
    init()
    try:
        user_guess: int = int(input(Fore.LIGHTBLUE_EX + 'Guess: '))
    except ValueError as e:
        print(Fore.LIGHTRED_EX + f'Please enter a valid number {e}.')
        continue

    if user_guess > random_number:
        print(Fore.LIGHTBLUE_EX + 'The number is lower!')
    elif user_guess < random_number:
        print(Fore.LIGHTBLUE_EX + 'The number is higher!')
    else:
        print(Fore.LIGHTYELLOW_EX + 'You guessed the correct number!')
        break
