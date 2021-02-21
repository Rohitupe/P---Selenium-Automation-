# Functional Test Suite
import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print("TC_PaymentTest - Payment In Dollar")
        self.assertTrue(True, "paymentInDollar - Test Have Problem")

    def test_paymentInRupees(self):
        print("TC_PaymentTest - Payment In Rupees")
        self.assertTrue(True, "paymentInRupees - Test Have Problem")


if __name__ == "__main__":
    unittest.main()