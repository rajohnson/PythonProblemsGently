import pytest
from odd_even import isEven, isOdd


@pytest.mark.parametrize("num", [-2, 0.5, 0, 4.2, 8, 100, 212, 1_000_000, 2.0])
def test_odd_with_not_odd(num: int) -> None:
    assert isOdd(num) is False


@pytest.mark.parametrize("num", [-1, 5, 7, 107, 219, 1_000_001, 3.0])
def test_odd_with_odd(num: int) -> None:
    assert isOdd(num) is True


@pytest.mark.parametrize("num", [-1, 0.5, 4.2, 5, 7, 107, 219, 1_000_001, 3.0])
def test_even_with_not_even(num: int) -> None:
    assert isEven(num) is False


@pytest.mark.parametrize("num", [-2, 0, 8, 100, 212, 1_000_000, 2.0])
def test_even_with_even(num: int) -> None:
    assert isEven(num) is True
