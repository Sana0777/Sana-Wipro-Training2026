import pytest
from Q2_calculator import add,sub,mul,div


@pytest.mark.parametrize("a,b,res", [
    (2, 3, 5),
    (10, 5, 15),
])
def test_add(a,b,res):
    assert add(a,b)==res

@pytest.mark.parametrize("a,b,res", [
    (5, 3, 2),
    (10, 5, 5),
])
def test_sub(a,b,res):
    assert sub(a,b)==res


@pytest.mark.parametrize("a,b,res", [
    (2, 3, 6),
    (-2, 3, -6),
    (10, 0, 0)
])
def test_mul(a,b,res):
    assert mul(a,b)==res


@pytest.mark.parametrize("a,b,res", [
    (10, 2, 5),
    (20, 4, 5),
])
def test_div(a,b,res):
    assert div(a,b)==res

def test_div_zero():
    with pytest.raises(ValueError):
        div(10, 0)
