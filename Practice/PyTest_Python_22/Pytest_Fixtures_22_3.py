import pytest
# @pytest.yield_fixture() - Example


@pytest.yield_fixture()  # run method before and after every test
def setup():
    print("run once before every test method")
    yield
    print("run once after every test method")


def testFirst():
    print("First test")


def testSecond(setup):
    print("Second Test")


def testThree(setup):
    print("Third Test")
    print("Not Running Setup method here")
