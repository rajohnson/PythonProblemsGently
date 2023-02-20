from typing import Sequence


def median(values: Sequence[float]) -> float | None:
    if len(values) == 0:
        return None

    sorted_values = sorted(values)
    middle_index = len(sorted_values) // 2

    if len(values) % 2 == 1:
        return sorted_values[middle_index]

    # if there are an even number of elements middle_index will be the larger of the
    # two indices that need to be averaged.
    # e.g for values = [1, 2, 3, 4], middle_index would be 2 and the other term
    # would be at index 1.
    return (sorted_values[middle_index] + sorted_values[middle_index - 1]) / 2
