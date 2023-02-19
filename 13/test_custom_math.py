import pytest
from custom_math import calculate_product, calculate_sum


@pytest.mark.parametrize("input_value", ((), []))
def test_sum_empty(input_value):
    assert calculate_sum(input_value) == 0


@pytest.mark.parametrize("input_value", ((), []))
def test_product_empty(input_value):
    assert calculate_product(input_value) == 1


@pytest.mark.parametrize("input_value, expected", [([2, 4, 6, 8, 10], 30), ([4], 4)])
def test_sum(input_value, expected):
    assert calculate_sum(input_value) == expected


@pytest.mark.parametrize("input_value, expected", [([2, 4, 6, 8, 10], 3840), ([4], 4)])
def test_product(input_value, expected):
    assert calculate_product(input_value) == expected
