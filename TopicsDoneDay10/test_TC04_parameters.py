import pytest

@pytest.mark.parametrize("a,b,res",[(2,3,5),(7,6,13)])
def test_add(a,b,res):
    print(a+b)
    assert a+b==res

@pytest.mark.smoke
def test_smoke():     ###by using pytest -m smoke i can run only smoke functions
    assert True

@pytest.mark.skip(reason="Not ready yet")
def test_skip():                            ###this will skip running a particular function
    pass
