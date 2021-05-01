import pytest

"""
1. if you want fixture to run after and before every test --> @pytest.fixture()
2. if you want to run fixture only once for each class like class level --> @pytest.fixture(scope="class")
"""


@pytest.fixture(scope="class")
def setup():
    print("Run before test")
    yield
    print("Run after test")
