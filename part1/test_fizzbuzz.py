import pytest
from .fizzbuzz import fizzbuzz

def test_positive_test_fizzbuzz_multiple_of_three_should_return_fizz():
    assert fizzbuzz(3) == 'Fizz'

def test_fizzbuzz_multiple_of_five_should_return_buzz():
    assert fizzbuzz(5) == 'Buzz'

def test_fizzbuzz_multiple_of_three_and_five_should_return_fizz_buzz():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzbuzz_not_multiple_of_three_or_five_should_return_number():
    assert fizzbuzz(4) == 4

def test_fizzbuzz_not_multiple_of_three():
    assert fizzbuzz(2) != "Fizz"

def test_fizzbuzz_not_multiple_of_five():
    assert fizzbuzz(7) != "Buzz"

def test_fizzbuzz_not_multiple_of_three_or_five_should_not_return_fizz_buzz():
    assert fizzbuzz(11) != "FizzBuzz"

def test_negative_pytest_array_invalid_type_should_throw_type_error():
    with pytest.raises(TypeError):
        fizzbuzz([1,2,3])

def test_string_should_throw_type_error():
    with pytest.raises(TypeError):
        fizzbuzz(["asdf"])
