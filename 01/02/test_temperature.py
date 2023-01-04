import temperature
import pytest


@pytest.mark.parametrize(
    "f, c",
    [(0, -17.77777777777778), (32, 0), (180, 82.22222222222223), (212, 100)],
)
def test_f_to_c(f, c):
    assert temperature.convertToCelsius(f) == c
