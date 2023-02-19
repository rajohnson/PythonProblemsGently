import pytest
import temperature


@pytest.mark.parametrize(
    "f, c",
    [(0, -17.77777777777778), (32, 0), (180, 82.22222222222223), (212, 100)],
)
def test_f_to_c(f, c):
    assert temperature.convertToCelsius(f) == c


@pytest.mark.parametrize(
    "c, f",
    [
        (0, 32),
        (50, 122),
        (100, 212),
    ],
)
def test_c_to_f(c, f):
    assert temperature.convertToFahrenheit(c) == f


@pytest.mark.parametrize(
    "start", [-100, -50, 0, 25, 50, 75, 100, 1000, 10_000]
)
def test_convert_round_trip_c_to_f_to_c(start):
    assert start == temperature.convertToCelsius(
        temperature.convertToFahrenheit(start)
    )


@pytest.mark.parametrize(
    "start", [-100, -50, 0, 25, 50, 75, 100, 1000, 10_000]
)
def test_convert_round_trip_f_to_c_to_f(start):
    assert start == temperature.convertToFahrenheit(
        temperature.convertToCelsius(start)
    )
