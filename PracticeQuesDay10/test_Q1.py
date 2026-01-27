import pytest
from Q1 import add

@pytest.mark.parametrize("a,b,res", [(2,3,5),(4,5,9)])
def test_add(a,b,res):
    print(a+b)
    assert add(a,b)==res