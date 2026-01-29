##Expected failure (xfail)
import pytest

@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5