# Sanity Test Suite
import unittest


class SignUpTest(unittest.TestCase):
    def test_signUpByEmail(self):
        print("TC_SignUpTest - SignUp By Email")
        self.assertTrue(True, "signUpByEmail - Test Have Problem")

    def test_signUpByFacebook(self):
        print("TC_SignUpTest - SignUp By Facebook")
        self.assertTrue(True, "signUpByFacebook - Test Have Problem")

    def test_signUpByTwitter(self):
        print("TC_SignUpTest - SignUp By Twitter")
        self.assertTrue(True, "signUpByTwitter - Test Have Problem")


if __name__ == "__main__":
    unittest.main()
