import pytest
import unittest
from .calculator import calculator

#Example Positive Test
def test_two_plus_three_should_return_five():
    assert calculator(2, 3) == 5

def test_one_hundred_plus_ninety_nine_should_return_one_hundred_ninety_nine():
    assert calculator(100, 99) == 199

def test_calculator_with_multiple_integers():
    assert calculator(6, 7, 18, 25) == 56

#Example Negative input throwing an Error
def test_negative_input_should_throw_error(self):
    with self.assertRaises(ValueError):
        calculator(6, 7, -18, 25)