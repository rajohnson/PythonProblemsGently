import pytest
from replace import findAndReplace


@pytest.mark.parametrize(
    "begin, target, replacement, end",
    [
        ("The fox", "fox", "dog", "The dog"),
        ("fox", "fox", "dog", "dog"),
        ("Firefox", "fox", "dog", "Firedog"),
        ("foxfox", "fox", "dog", "dogdog"),
        ("The Fox and fox", "fox", "dog", "The Fox and dog"),
        ("forget about the fox", "fox", "dog", "forget about the dog"),
    ],
)
def test_replace(begin, target, replacement, end):
    assert findAndReplace(begin, target, replacement) == end
