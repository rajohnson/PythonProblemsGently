from fizzbuzz import fizzBuzz, fizzbuzz_of
import pytest


@pytest.mark.parametrize("num", [-1, 1, 2, 4, 7, 8, 11, 13, 14])
def test_fizzbuzz_non_multiples(num):
    assert fizzbuzz_of(num) == num


@pytest.mark.parametrize("num", [-5, 5, 10, 20, 25, 35, 40])
def test_fizzbuzz_multiples_of_5(num):
    assert fizzbuzz_of(num) == "Buzz"


@pytest.mark.parametrize("num", [-3, 3, 6, 9, 12, 18, 21])
def test_fizzbuzz_multiples_of_3(num):
    assert fizzbuzz_of(num) == "Fizz"


@pytest.mark.parametrize("num", [-15, 15, 30, 150, 3000])
def test_fizzbuzz_multiples_of_15(num):
    assert fizzbuzz_of(num) == "FizzBuzz"


def test_fizzbuzz(capsys):
    fizzBuzz(15)
    result = capsys.readouterr().out
    expected = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\n"
    assert result == expected
