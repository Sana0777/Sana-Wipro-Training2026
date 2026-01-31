import pytest

@pytest.mark.parametrize("a, b, res", [
    (2, 3, 5),
    (5, 5, 10),
    (10, 0, 10),
])
def test_addition(a, b, res):
    assert a + b == res

def test_environment(env):
    assert env in ["a", "b", "c"]

@pytest.mark.skip(reason="Not ready")
def test_skip_example():
    assert False

@pytest.mark.xfail(reason="Known issue")
def test_xfail_example():
    assert 10 / 0 == 5

@pytest.mark.skipif(
    pytest.__version__.startswith("6"),
    reason="Version issue"
)
def test_version_check():
    assert True
