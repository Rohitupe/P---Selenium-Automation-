import unittest

class TestAssertInORNotIn(unittest.TestCase):
    def test_First(self):
        lists = ["Python", "Java", "C#", "Perl", "JavaScript"]
        # it will search whether element is in container or not
        # self.assertIn("Python", lists, "member not found in container")

        # it will search whether element is not in container
        # self.assertNotIn("C++", lists, "Member Not Found")


if __name__ == "__main__":
    unittest.main()