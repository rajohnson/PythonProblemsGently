import string

import pytest
from hypothesis import given, strategies
from password import SPECIAL_CHARACTERS, generate_password


@given(
    strategies.integers(min_value=1, max_value=512),
    strategies.random_module(),
)
def test_password(n: int, rnd) -> None:
    password = generate_password(n)
    password_set = set(password)
    assert len(password) == n if n >= 12 else 12

    num_lowercase = len(password_set.intersection(set(string.ascii_lowercase)))
    assert num_lowercase >= 1

    num_uppercase = len(password_set.intersection(set(string.ascii_uppercase)))
    assert num_uppercase >= 1

    num_special = len(password_set.intersection(set(SPECIAL_CHARACTERS)))
    assert num_special >= 1

    num_digits = len(password_set.intersection(set(string.digits)))
    assert num_digits >= 1


def test_password_short() -> None:
    assert len(generate_password(8)) == 12


@pytest.mark.repeat(20)
def test_password_has_all_chars() -> None:
    password = generate_password(14)
    assert len(password) == 14
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch in string.ascii_lowercase:
            has_lowercase = True
        if ch in string.ascii_uppercase:
            has_uppercase = True
        if ch in string.digits:
            has_digit = True
        if ch in SPECIAL_CHARACTERS:
            has_special = True
    assert has_lowercase and has_uppercase and has_digit and has_special
