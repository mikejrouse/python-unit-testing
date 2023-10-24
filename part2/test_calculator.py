import pytest
from .calculator import calculator

#Example Positive Test
def test_two_plus_three_should_return_five():
    assert calculator(2, 3) == 5

# def test_100_plus_99_should_equal_199():
def test_one_hundred_plus_ninety_nine_should_return_one_hundred_ninety_nine():
    assert calculator(100, 99) == 199

# def test_6_plus_7_plus_18_plus_25_should_equal_56():
def test_six_plus_seven_plus_eighteen_plus_twenty_five_should_return_fifty_six():
    assert calculator(6, 7, 18, 25) == 56