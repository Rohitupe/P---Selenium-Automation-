import unittest


def setUpModule():  # module level test
    print("This is Module")

def tearDownModule():  # module level test
    print("The is module teardown")


# Class One
class OneClassTest(unittest.TestCase):  # class level test
    @classmethod
    def setUpClass(cls):
        print("Class Running of Class_1")

    def setUp(self):
        print("\t-Set Up Running of Class_1")

    def test_method_1(self):
        print("\t\tClass 1 Test Method 1")

    def test_method_2(self):
        print("\t\tClass 1 Test Method 2")

    def test_method_3(self):
        print("\t\tClass 1 Test Method 3")

    def tearDown(self):
        print("\t=Method Closing of Class_1\n")

    @classmethod
    def tearDownClass(cls):
        print("Class Closing of Class_1")


if __name__ == "__main__":
    unittest.main()
