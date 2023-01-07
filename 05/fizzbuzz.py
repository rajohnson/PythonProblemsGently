from typing import Union


def fizzbuzz_of(num: int) -> Union[int, str]:
    result: Union[int, str] = num
    if num % 15 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    return result


def fizzBuzz(end: int) -> None:
    """
    Print fizzbuzz for all numbers from 1 to end inclusive.
    For example fizzBuzz(15) = '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz\n'
    """
    print(" ".join(str(fizzbuzz_of(n)) for n in range(1, end + 1)))
