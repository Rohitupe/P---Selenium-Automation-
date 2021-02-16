from selenium import webdriver
import unittest


class SetupTearDownTest(unittest.TestCase):
    def setUp(self):
        print("Setup Running")

    def test_test1(self):
        print("Running Test 1")

    def test_test2(self):
        print("Running Test 2")

    def tearDown(self):
        print("Close Everything")


if __name__ == "__main__":
    unittest.main()
