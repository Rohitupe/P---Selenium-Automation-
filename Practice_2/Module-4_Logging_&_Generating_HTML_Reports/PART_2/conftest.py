from _pytest.fixtures import yield_fixture
import pytest

@pytest.fixture()
def loadData():
    first_name = "Rohit"
    last_name = "Tupe"
    return [first_name, last_name]