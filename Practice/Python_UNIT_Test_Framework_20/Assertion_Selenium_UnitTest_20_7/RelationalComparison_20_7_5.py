import unittest

class TestRelationComparison(unittest.TestCase):
    def test_First(self):
        # check whether 4 > 5 or not
        self.assertGreater(4, 5, "Not Greater")
        # self.assertGreaterEqual(5, 5, "greater or equal")

        # check whether 4 < 5 or not
        # self.assertLess(4, 5, "not less than")
        # self.assertLessEqual(4, 4, "Equal or less")

if __name__ == "__main__":
    unittest.main()