import pytest

@pytest.fixture(scope="function")
def sample_numbers():
    print("\nSetup: sample_numbers")
    return (10, 5)
