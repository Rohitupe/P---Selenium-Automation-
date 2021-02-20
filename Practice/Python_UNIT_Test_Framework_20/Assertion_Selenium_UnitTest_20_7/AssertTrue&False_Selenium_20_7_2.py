import unittest
from selenium import webdriver

class TestTrueFalse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge("../../../Driver/msedgedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_TrueFalse(self):
        self.driver.get("https://www.google.com")
        self.title = self.driver.title
        print(self.title)

        # assertTrue
        # self.assertTrue(self.title == "Google", "True Testcase")

        # assertFalse
        # self.assertFalse(self.title == "Googlee", "False Testcase")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()