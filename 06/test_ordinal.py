import pytest
from ordinal import ordinalSuffix


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, "0th"),
        (1, "1st"),
        (2, "2nd"),
        (3, "3rd"),
        (4, "4th"),
        (5, "5th"),
        (6, "6th"),
        (7, "7th"),
        (8, "8th"),
        (9, "9th"),
        (10, "10th"),
        (11, "11th"),
        (12, "12th"),
        (13, "13th"),
        (14, "14th"),
        (101, "101st"),
    ],
)
def test_ordinal(num: int, expected: str) -> None:
    assert ordinalSuffix(num) == expected
