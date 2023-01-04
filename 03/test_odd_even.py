from odd_even import isOdd, isEven
import pytest


@pytest.mark.parametrize("num", [-2, 0.5, 0, 4.2, 8, 100, 212, 1_000_000, 2.0])
def test_odd_with_not_odd(num):
    assert isOdd(num) == False


@pytest.mark.parametrize("num", [-1, 5, 7, 107, 219, 1_000_001, 3.0])
def test_odd_with_odd(num):
    assert isOdd(num) == True


@pytest.mark.parametrize("num", [-1, 0.5, 4.2, 5, 7, 107, 219, 1_000_001, 3.0])
def test_even_with_not_even(num):
    assert isEven(num) == False


@pytest.mark.parametrize("num", [-2, 0, 8, 100, 212, 1_000_000, 2.0])
def test_even_with_even(num):
    assert isEven(num) == True
