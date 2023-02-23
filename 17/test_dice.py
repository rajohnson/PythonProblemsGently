import pytest
from dice import SIDES, roll_dice
from hypothesis import given, strategies


# This essentially duplicates test_roll_dice, but it is here for experimentation
# with property based testing.
@given(strategies.integers(min_value=1, max_value=1000))
def test_dice_in_range(n: int) -> None:
    roll = roll_dice(n)

    assert roll >= n
    assert roll <= n * SIDES


@pytest.mark.repeat(5)
def test_roll_dice_changes() -> None:
    result_set = set(roll_dice(1) for _ in range(100))
    assert len(result_set) != 1


@pytest.mark.repeat(5)
@pytest.mark.parametrize("num_dice", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000])
def test_roll_dice(num_dice: int) -> None:
    possible_range = range(num_dice * 1, (num_dice * SIDES) + 1)
    assert roll_dice(num_dice) in possible_range
