import pytest
# @pytest.fixture() - Example


@pytest.fixture()  # run method only once before test method
def setup():
    print("run only once - before test method")


def testFirst(setup):
    print("First test")


def testSecond(setup):
    print("Second Test")


def testThree():
    print("Third Test")
    print("Not Running Setup method here")
