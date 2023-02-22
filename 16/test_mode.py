import random
from typing import Sequence

import pytest
from mode import mode


@pytest.mark.parametrize(
    "values, expected",
    [([], None), ([1], 1), ([1, 2, 3, 4, 4], 4), ([1, 1, 2, 3, 4], 1)],
)
def test_mode(values: Sequence[float], expected: float | None) -> None:
    assert mode(values) == expected


def test_mode_order_independent() -> None:
    test_values = [1, 1, 1, 1, 1, 2]
    random.seed(42)
    for _ in range(100):
        random.shuffle(test_values)
        assert mode(test_values) == 1
