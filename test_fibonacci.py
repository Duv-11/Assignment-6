"""Assignment 6 - a fibonacci series iterable
Devon Singh 2025/07/27"""

import pytest
from fibonacci import Fibonacci

def test_integer_input():
    with pytest.raises(ValueError):
        list(Fibonacci("ten"))
    with pytest.raises(ValueError):
        list(Fibonacci(3.5))

def test_zero_value():
    assert list(Fibonacci(0)) == [0]

def test_value_one():
    assert list(Fibonacci(1)) == [0, 1]

def test_value_two():
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_value_four():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]

def test_value_ten():
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_negative_value():
    assert list(Fibonacci(-5)) == []
