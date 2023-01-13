from time_str import getHoursMinutesSeconds
import pytest


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (30, "30s"),
        (60, "1m"),
        (90, "1m 30s"),
        (3600, "1h"),
        (3601, "1h 1s"),
        (3661, "1h 1m 1s"),
        (90042, "25h 42s"),
        (0, "0s"),
    ],
)
def test_getHoursMinutesSeconds(seconds, expected):
    assert getHoursMinutesSeconds(seconds) == expected
