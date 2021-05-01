import pytest

""" to run in terminal --> pytest -m smoke -v -s """


# marking test with name smoke
@pytest.mark.smoke
def test_one():
    print("This is marked test 1")


def test_two():
    print("Unmarked Test")


# marking test with name smoke
@pytest.mark.smoke
def test_three():
    print("This is marked test 3")
