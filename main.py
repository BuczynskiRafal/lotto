"""
The module includes functions that allow
you to calculate the number of draws,
the cost of draws and the time needed
to hit 6 in the lotto.
"""
import random
from typing import Set


WEEKS_OF_YEAR = 52
GAME_COST = 3


def get_six_random_numbers() -> Set[int]:
    """Draw 6 numbers.

    :return: list: Sorted list of six numbers.
    """
    return set(random.sample(range(1, 50), k=6))


def how_many_draws_to_hit_six() -> int:
    """Calculate how many times you have to play to hit 6 lottery numbers,
     always playing with the same numbers.

    :return:
    str: The number of draws, the cost of tickets and the time needed to win are given in years.
    """
    counter = 1
    cross_number = get_six_random_numbers()
    while True:
        lotto_draw = get_six_random_numbers()
        if not cross_number == lotto_draw:
            counter += 1
        else:
            return counter


if __name__ == '__main__':
    print("Skreślam liczby i obliczam ile razy należy wykonać losowanie "
          "aby trafić szóstkę stosujac przeudolosowe liczby "
          "(zakładając że obstawiane liczny się nie zmieniają).")
    count = how_many_draws_to_hit_six()
    print(f"Ilość losowań: {count:,}, "
          f"koszt wszytskich losowań: {count * 3:,} pln, "
          f"lata potrzebne żeby trafić 6: {count/WEEKS_OF_YEAR:.0f} lat")
