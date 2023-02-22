import pytest
from dice import SIDES, roll_dice

# this would be a decent spot to use hypothesis for the tests


@pytest.mark.repeat(5)
def test_roll_dice_changes() -> None:
    result_set = set(roll_dice(1) for _ in range(100))
    assert len(result_set) != 1


@pytest.mark.repeat(5)
@pytest.mark.parametrize("num_dice", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000])
def test_roll_dice(num_dice: int) -> None:
    possible_range = range(num_dice * 1, (num_dice * SIDES) + 1)
    assert roll_dice(num_dice) in possible_range
