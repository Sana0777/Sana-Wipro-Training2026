import pytest

@pytest.fixture
def data():
    return [1,2,3]

def test_1(data):
    #data=[1,2,3]
    assert 2 in data

def test_2(data):
   # data=[1,2,3]
    assert len(data)==3