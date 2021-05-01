import pytest
"""
  pass setup method only once then it will applied to every test in the class by using usefixtures decorator
"""


@pytest.mark.usefixtures("setup")
class TestSetupRun:
    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")

    def test_three(self):
        print("test three")

    def test_four(self):
        print("test four")

    def test_five(self):
        print("test five")
