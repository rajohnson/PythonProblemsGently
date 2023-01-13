from minmax import getSmallest
import pytest


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
def test_getSmallest(values, expected):
    assert getSmallest(values) == expected
