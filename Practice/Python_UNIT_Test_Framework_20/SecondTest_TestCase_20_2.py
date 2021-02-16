import unittest
from selenium import webdriver


# Search Engine Test
class SearchEngineTest(unittest.TestCase):

    def test_Google(self):
        self.driver = webdriver.Chrome("../../Driver/chromedriver.exe")
        self.driver.get("https://www.google.com")
        print("Title of the web page is " + self.driver.title)
        self.driver.close()

    def test_DuckDuckGo(self):
        self.driver = webdriver.Edge("../../Driver/msedgedriver.exe")
        self.driver.get("https://www.duckduckgo.com")
        print("Title of the page is " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
