import unittest


class AppTesting(unittest.TestCase):
    def test_search(self):
        print("Searching Tests")

    @unittest.skip("This is reason based skipping test")  # skip with reason
    def test_advanceSearch(self):
        print("Doing Advance Search")

    def test_prepaidRecharge(self):
        print("Prepaid Recharge is working")

    @unittest.SkipTest  # skip this test --> Simple way
    def test_postPaidRecharge(self):
        print("This is PostPaid Recharge")

    def test_loginByGmail(self):
        print("Gmail Login")

    @unittest.skipIf(1 == 1, "This is conditional based skipping")  # conditional based skip test
    def test_loginByTwitter(self):
        print("Twitter Login")


if __name__ == "__main__":
    unittest.main()
