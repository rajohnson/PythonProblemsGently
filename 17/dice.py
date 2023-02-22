import random

SIDES = 6


def roll_dice(num_dice: int) -> int:
    # for large values of num_dice it would be more efficient to calculate the possible
    # range and randomly choose from it rather than summing the results of single rolls
    return sum(random.choice(range(1, SIDES + 1)) for _ in range(num_dice))
