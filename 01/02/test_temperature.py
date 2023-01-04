import temperature
import pytest


@pytest.mark.parametrize("f, c", [(32, 0)])
def test_f_to_c(f, c):
    assert temperature.convertToCelsius(f) == c
