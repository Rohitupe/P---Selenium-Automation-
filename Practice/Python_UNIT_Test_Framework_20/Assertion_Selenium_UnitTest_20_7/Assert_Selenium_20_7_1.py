import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_FirstTest(self):
        driver = webdriver.Edge("../../../Driver/msedgedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.google.com")
        web_title = driver.title
        print(web_title)
        # equal assertion
        # self.assertEqual("Google", web_title, "Title is not same")

        # not equal assertion
        self.assertNotEqual("Google", web_title, "Title is not same test passed")


if __name__ == "__main__":
    unittest.main()
