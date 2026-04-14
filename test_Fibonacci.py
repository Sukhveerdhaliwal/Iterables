import pytest
from Fibonacci import fibonacci

def test_invalid_input():
    with pytest.raises(ValueError):
        fibonacci("Input is not an integer")
def test_negative_input():
    assert list(fibonacci(-1)) == []
def test_zero_input():
    assert list(fibonacci(0)) == [0]
def test_one_input():
    assert list(fibonacci(1)) == [0, 1]
def test_two_input():
    assert list(fibonacci(2)) == [0, 1, 1]
def test_four_input():
    assert list(fibonacci(4)) == [0, 1, 1, 2, 3]
def test_ten_input():
    assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


