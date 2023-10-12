# Exercise 7 Python Unit Testing

Welcome to exercise 7 Year of the Engineer Python coding session. This session is all about unit testing! There will be 2 parts to this session but before we get into the exercises, here is some background on unit testing:

## What is Unit testing?

Unit tests are small pieces of code that test each individual unit of the program that you are writing. We want to write unit tests as we develop software to ensure that our code is functioning as intended and these test should run automatically as part of building our code. There are 2 types of unit tests, positive and negative. Positive unit tests are written to test our code when we give it valid inputs, and negative unit tests are written to test our code when we give it inputs that should be invalid. There are many benefits of writing unit tests, especially as developers keep adding to a code base and it gets older and more complex:

1. Early Bug Detection: When we write unit tests as we develop our code, we can catch bugs as we write them so they don't affect features that are developed later.
2. Code Quality/Confidence: When we have a suite of unit tests testing every piece of our code, we can be confident that we have written quality code and we will find few unexpected bugs.
3. Built in regression testing: When we have a full suite of unit tests in a code base that run automatically, we can be sure that any change we make to that code base doesn't break any existing functionality.
4. Documentation: A full test suite also functions as living documentation of a code base so any developer can look at the unit tests for a project and be able to see what each piece of that project does.

## Test Driven Development (TDD)

One of the accepted best practices for writing unit tests is a practice called Test Driven Development where you write the tests for your code before you write your code based on your acceptance criteria. TDD is great for ensuring that you are writing simple code that meets all the requirements of your project. The Test Driven Development or "Red-Green-Clean" development cycle is as follows:

1. Examine the Acceptance Criteria of a project
2. Add both positive and negative tests to your test suite
3. Run all the tests to make sure that they fail
4. Write code to make a single test pass and re-run all the tests
5. Refactor the code you just wrote to be as simple and readable as possible
6. Repeat until all tests pass

## Session 7 Part 1 - FizzBuzz

In the first part of this session, you will be given a program called FizzBuzz and be expected to write both positive and negative unit tests for it. FizzBuzz is a common beginners python exercise where one is supposed to write a program that loops through a range of integers and returns "Fizz" for multiples of 3, returns "Buzz" for multiples of 5, and returns "FizzBuzz" for multiples of 3 and 5. The first test will be written for you.

## Session 7 Part 2 - Calculator with TDD

In this part, you will be creating a simple calculator using TDD following the steps below. For each of the steps below, please follow the TDD cycle and try not to read ahead. For each of the steps, remember to write both positive and negative tests as you see fit. As you progress, try to modify previous tests as little as possible while still making sure they pass and watch your test suite grow!

1. Write tests and a method called add that takes 2 ints as parameters and adds them together.
2. Now modify that method to take any amount of integers
3. Now have add() throw an Error when a negative number is passed in
4. Now write a new method called operation() that takes a string with the value "add", "subtract", "mulitply", or "divide" and 2 integers as parameters that calculates the result of the operation applied to the 2 integers. Return a message informing the user that the operation is not supported if the string is not a supported operation.
    Ex. `operation("multiply", 3, 3)` should return 9 and `operation("unsupported", 1, 2)` should return an error message

## Libraries

- pytest

## Setup and Running Tests

To set up the project, run `python -m venv .venv` in the root directory of this projects, then activate your virtual environment and run `pip install -r requirements.txt` to install pytest in your virtual environment.

To run tests, simply run `pytest <path_to_testfile>`

## References

- [Overview of Unit Testing](https://www.geeksforgeeks.org/unit-testing-software-testing/)
- [Test Driven Development](https://testdriven.io/test-driven-development/)
- [PEP 008](https://peps.python.org/pep-0008/)
- [reST Docstrings](https://sweetpea-org.github.io/guide/contributing/rest_style_guide.html)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)