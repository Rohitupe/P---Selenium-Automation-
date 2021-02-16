from selenium import webdriver
import unittest


class SetupTearDownTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Running")

    def test_test1(self):
        print("Running Test 1")

    def test_test2(self):
        print("Running Test 2")

    @classmethod
    def tearDownClass(cls):
        print("Close Everything")


if __name__ == "__main__":
    unittest.main()
