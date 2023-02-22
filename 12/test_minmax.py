from typing import Sequence

import pytest
from minmax import getLargest, getSmallest


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3], 1),
        ([3, 2, 1], 1),
        ((3, 2, 1), 1),
        ([28, 25, 42, 2, 28], 2),
        ([1], 1),
        ([], None),
    ],
)
def test_getSmallest(values: Sequence[int], expected: int | None) -> None:
    assert getSmallest(values) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3], 3),
        ([3, 2, 1], 3),
        ((3, 2, 1), 3),
        ([28, 25, 42, 2, 28], 42),
        ([1], 1),
        ([], None),
    ],
)
def test_getLargest(values: Sequence[int], expected: int | None) -> None:
    assert getLargest(values) == expected
