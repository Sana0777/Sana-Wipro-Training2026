import pytest
@pytest.fixture
def setup_teardown():
    print("\nsetup")
    yield
    print("teardown")


def test_example1(setup_teardown):
    print("test1_example")

def test_example2(setup_teardown):
    print("test2_example")