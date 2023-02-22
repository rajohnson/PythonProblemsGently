import random
from typing import Sequence

import pytest
from average import average


@pytest.mark.parametrize(
    "input_values, expected",
    [
        ([1, 2, 3], 2),
        ([1, 2, 3, 1, 2, 3, 1, 2, 3], 2),
        ([12, 20, 37], 23),
        ([0, 0, 0, 0, 0, 0], 0),
    ],
)
def test_average(input_values: Sequence[float], expected: float | None) -> None:
    assert average(input_values) == expected


def test_order_independent() -> None:
    random.seed(42)
    test_data = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    for _ in range(100):
        random.shuffle(test_data)
        assert average(test_data) == 2
