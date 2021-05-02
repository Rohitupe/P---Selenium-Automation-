from _pytest.fixtures import yield_fixture
import pytest


@pytest.fixture(scope="class")
def setup():
    """ This is setup method will run every time for every class """
    print("This is setup method")
    yield
    print("Setup Method ends here")


# data to be laod in the fixtures for processing test cases
@pytest.fixture()
def loadData():
    """ This acts as a fixture to load data for test cases """
    first_name = "Rohit"
    last_name = "Tupe"
    website = "https://www.google.com"

    return [first_name, last_name, website]
