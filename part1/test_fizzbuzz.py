import pytest
from .fizzbuzz import fizzbuzz

#Example Positive Test
def test_multiple_of_three_should_return_fizz():
    assert fizzbuzz(3) == 'Fizz'

# def test_multipleOfFive_shouldReturnBuzz():
def test_multiple_of_five_should_return_buzz():
    assert fizzbuzz(5) == 'Buzz'

# def test_multipleOfThreeAndFive_shouldReturnFizzBuzz():

# def test_notMultipleOfThreeOrFive_shouldReturnNumber():

# def test_notMultipleOfThreeOrFive_shouldNotReturnFizz():

# def test_notMultipleOfThreeOrFive_shouldNotReturnBuzz():

# def test_notMultipleOfThreeOrFive_shouldNotReturnFizzBuzz():

#Example Negative test throwing an Error
def test_array_shouldThrowTypeError():
    with pytest.raises(TypeError):
        fizzbuzz([1,2,3])

# def test_string_shouldThrowTypeError():