import unittest
from selenium import webdriver

class TestIsNoneORNotNone(unittest.TestCase):
    def test_First(self):
        driver = webdriver.Edge(executable_path="../../../Driver/msedgedriver.exe")
        # To check whether it is None
        # self.assertIsNone(driver, "Driver variable is Not None")

        # self.assertIsNotNone(driver, "Driver variable is None")

if __name__ == "__main__":
    unittest.main()