import pytest
from coffee import get_cost_of_coffee


@pytest.mark.parametrize(
    "number, cost, total",
    [
        (7, 2.5, 17.5),
        (8, 2.5, 20),
        (9, 2.5, 20),
        (10, 2.5, 22.5),
        (17, 1, 16),
        (18, 1, 16),
        (19, 1, 17),
    ],
)
def test_get_cost_of_coffee(number: int, cost: float, total: float) -> None:
    assert get_cost_of_coffee(number, cost) == total
