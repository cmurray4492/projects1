"""Dice Program"""
import random


def roll_dice(amount: int = 2) -> list[int]:
    '''Random dice roll, amount in is number of dice'''
    if amount <= 0:
        raise ValueError

    cdm: int = 0
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
        cdm = cdm + random_roll
    print(f"Total of rolls = {cdm}")

    return rolls


def main():
    '''Main dice function'''
    while True:
        try:
            user_input: str = input('How many dice do you want to roll? ')

            if user_input.lower() == 'exit':
                print('Thanks for playing')
                break

            print(*roll_dice(int(user_input)), sep=', ')

        except ValueError:
            print('Please enter a valid number!')


if __name__ == '__main__':
    main()
