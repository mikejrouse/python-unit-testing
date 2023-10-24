import pytest
from .fizzbuzz import fizzbuzz

#Example Positive Test
def test_multiple_of_three_should_return_fizz():
    assert fizzbuzz(3) == 'Fizz'

# def test_multipleOfFive_shouldReturnBuzz():
def test_multiple_of_five_should_return_buzz():
    assert fizzbuzz(5) == 'Buzz'

# def test_multipleOfThreeAndFive_shouldReturnFizzBuzz():
def test_multiple_of_three_and_five_should_return_fizz_buzz():
    assert fizzbuzz(15) == 'FizzBuzz'

# def test_notMultipleOfThreeOrFive_shouldReturnNumber():
def test_not_multiple_of_three_or_five_should_return_number():
    assert fizzbuzz(4) == 4

# def test_notMultipleOfThreeOrFive_shouldNotReturnFizz():
def test_not_multiple_of_three_or_five_should_not_return_fizz():
    assert fizzbuzz(2) != "Fizz"

# def test_notMultipleOfThreeOrFive_shouldNotReturnBuzz():
def test_not_multiple_of_three_or_five_should_not_return_buzz():
    assert fizzbuzz(7) != "Buzz"

# def test_notMultipleOfThreeOrFive_shouldNotReturnFizzBuzz():
def test_not_multiple_of_three_or_five_should_not_return_fizz_buzz():
    assert fizzbuzz(11) != "FizzBuzz"

#Example Negative test throwing an Error
def test_array_should_throw_type_error():
    with pytest.raises(TypeError):
        fizzbuzz([1,2,3])

# def test_string_should_throw_type_error():
def test_string_should_throw_type_error():
    with pytest.raises(TypeError):
        fizzbuzz(["asdf"])