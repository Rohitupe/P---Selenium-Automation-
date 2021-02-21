# Sanity Test Suite
import unittest


class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("TC_LoginTest - Login By Email")
        self.assertTrue(True, "loginByEmail - Test Have Problem")

    def test_loginByFacebook(self):
        print("TC_LoginTest - Login By Facebook")
        self.assertTrue(True, "loginByFacebook - Test Have Problem")

    def test_loginByTwitter(self):
        print("TC_LoginTest - Login By Twitter")
        self.assertTrue(True, "loginByTwitter - Test Have Problem")


if __name__ == "__main__":
    unittest.main()
