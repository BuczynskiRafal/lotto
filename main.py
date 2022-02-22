"""
The module includes functions that allow
you to calculate the number of draws,
the cost of draws and the time needed
to hit 6 in the lotto.
"""
import random
from typing import List


WEEKS_OF_YEAR = 52
GAME_COST = 3


def get_six_random_numbers() -> List[int]:
    """Draw 6 numbers.

    :return: list: Sorted list of six numbers.
    """
    numbers = []
    while len(numbers) != 6:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)


def how_many_draws_to_hit_six() -> str:
    """Calculate how many times you have to play to hit 6 lottery numbers.

    :return:
    str: The number of draws, the cost of tickets and the time needed to win are given in years.
    """
    counter = 0
    while True:
        cross_number = get_six_random_numbers()
        lotto_draw = get_six_random_numbers()
        if not cross_number == lotto_draw:
            counter += 1
            print(counter)
        else:
            return f"Ilość losowań: {counter}, " \
                   f"koszt wszytskich losowań: {counter * 3} pln, " \
                   f"lata potrzebne żeby trafić 6: {counter/WEEKS_OF_YEAR:.0f} lat"


if __name__ == '__main__':
    how_many_draws_to_hit_six()
