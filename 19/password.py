import random
import string

MINIMUM_LENGTH = 12
SPECIAL_CHARACTERS = "~!@#$%^&*()_+."


def generate_password(length: int) -> str:
    """
    Generate a sequence of random characters and return them.
    If the requested length is less than MINIMUM_LENGTH, then
    MINIMUM_LENGTH characters will be returned instead.
    """
    if length < MINIMUM_LENGTH:
        length = MINIMUM_LENGTH

    character_categories = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        SPECIAL_CHARACTERS,
    )
    possible = string.ascii_letters + SPECIAL_CHARACTERS + string.digits

    password_chars = [random.choice(category) for category in character_categories] + [
        random.choice(possible) for _ in range(length - len(character_categories))
    ]
    random.shuffle(password_chars)
    return "".join(password_chars)
