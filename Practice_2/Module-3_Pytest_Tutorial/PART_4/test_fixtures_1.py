import pytest
# Fixtures Tutorials
"""
  before yield keyword it is tearup method
  after yield keyword it is teardown method
"""


@pytest.fixture()
def setup():
    print("This is Tear Up method")
    yield
    print("This is Tear Down method")


def test_firstMethod(setup):
    print("First test method")


def test_secondMethod(setup):
    print("Second test method")
