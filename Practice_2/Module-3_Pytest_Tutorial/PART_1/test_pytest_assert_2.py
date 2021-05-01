import pytest

# to run this file in terminal type
#  --> pytest filename.py


def test_assert_check():
    """ assert condition without message """
    message = "Hi"
    assert message == "Hi"


def test_assert_message():
    """ assert message with condition """
    message = "Hello"
    assert message == "Hi", "Test Failed becoz condition does not match"


def test_cred_part1():
    print("test pytest assert 2 --> part 1")
