import py
import pytest

""" to run in terminal --> pytest -m regression -v -s """


# marking test with name regression
@pytest.mark.regression
def test_one_mark():
    print("This is marked and Regression Test")


# skip test and don't show warnings or any message related to this tes in console
@pytest.mark.regression
@pytest.mark.xfail
def test_two_mark():
    print("This is un marked test")


# skip this test with marked
@pytest.mark.regression
@pytest.mark.skip
def test_three_skip():
    print("we are oing to skip this test")
