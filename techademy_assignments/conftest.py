import pytest

def pytest_addoption(parser):
    parser.addoption("--env", default="a")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("env")
