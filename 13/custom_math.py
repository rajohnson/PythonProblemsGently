from typing import Iterable


def calculate_sum(values: Iterable[float]) -> float:
    result = 0.0
    for value in values:
        result += value
    return result


def calculate_product(values: Iterable[float]) -> float:
    result = 1.0
    for value in values:
        result *= value
    return result
