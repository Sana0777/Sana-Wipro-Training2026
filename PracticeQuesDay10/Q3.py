import pytest

def is_even(num):
    if not isinstance(num,int):
        raise ValueError("only integers are accepted")

    return num%2==0

def test_even():
    assert is_even(2) is True

def test_odd():
    assert is_even(5) is False

def test_invalid():
    with pytest.raises(ValueError):
        is_even("abc")



