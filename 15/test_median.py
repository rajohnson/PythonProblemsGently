import random

import pytest
from median import median


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], None),
        ([1], 1),
        ([1, 2, 3], 2),
        ([3, 7, 10, 4, 1, 9, 6, 5, 2, 8], 5.5),
        ([3, 7, 10, 4, 1, 9, 6, 2, 8], 6),
    ],
)
def test_median(values, expected):
    assert median(values) == expected


def test_median_order_independent():
    test_values = [3, 7, 10, 4, 1, 9, 6, 2, 8]
    random.seed(42)
    for _ in range(100):
        random.shuffle(test_values)
        assert median(test_values) == 6
