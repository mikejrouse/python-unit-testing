import unittest
from .calculator import calculator, operation

def test_positive_test_two_plus_three_should_return_five():
    assert calculator(2, 3) == 5

def test_one_hundred_plus_ninety_nine_should_return_one_hundred_ninety_nine():
    assert calculator(100, 99) == 199

def test_calculator_with_multiple_integers():
    assert calculator(6, 7, 18, 25) == 56

def test_negative_input_should_throw_value_error():
    with unittest.TestCase().assertRaises(ValueError):
        calculator(6, 7, -18, 25)

def test_operation_multiply():
    assert operation("multiply", 3, 3) == 9

def test_invalid_input_should_return_unsupported_operation():
    assert operation("unsupported", 1, 2) == "Unsupported operation"

def test_division_by_zero_not_allowed():
    assert operation("divide", 10, 0) == "Division by zero is not allowed."
