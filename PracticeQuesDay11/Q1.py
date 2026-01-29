###Assert Statements and Exceptions

def test_addition():
    assert 2 + 3 == 5

##Assert with message
def test_subtraction():
    assert 5 - 3 == 1, "Subtraction result is incorrect"

import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)