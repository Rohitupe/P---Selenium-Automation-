import pytest
""" load data and run tests """


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("loadData")
class TestData:
    def test_one(self):
        print("test one")

    def test_editProfile(self, loadData):
        print(loadData)
