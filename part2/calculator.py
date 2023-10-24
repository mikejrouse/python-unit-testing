#Create a calculator using the Test Driven Development cycle following the steps below. 
# 
# 1. Write tests and a method called add that takes 2 ints as parameters and adds them together.
# 2. Now modify that method to take any amount of integers
# 3. Now have add() throw an Error when a negative number is passed in
# 4. Now write a new method called operation() that takes a string with the value "subtract", "mulitply", or "divide" and 2 integers as parameters that calculates the result of the operation applied to the 2 integers. Return a message informing the user that the operation is not supported if the string is not a supported operation.

from typing import List

def calculator(*args: List[int]) -> int:
    if any(x < 0 for x in args):
        raise ValueError("Input must not contain negative integers")
    return sum(args)
