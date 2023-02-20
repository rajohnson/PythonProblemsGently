import random

import pytest
from mode import mode


@pytest.mark.parametrize(
    "values, expected",
    [([], None), ([1], 1), ([1, 2, 3, 4, 4], 4), ([1, 1, 2, 3, 4], 1)],
)
def test_mode(values, expected):
    assert mode(values) == expected


def test_mode_order_independent():
    test_values = [1, 1, 1, 1, 1, 2]
    random.seed(42)
    for _ in range(100):
        random.shuffle(test_values)
        assert mode(test_values) == 1
