import pytest

@pytest.fixture
def list_positive():
    return [11, 22, 33, 44, 55]

@pytest.fixture
def list_negative():
    return [-11, -22, -33, -44, -55]

@pytest.fixture
def list_nulls():
    return [0, 0, 0, 0, 0]

@pytest.fixture
def list_none():
    return None

