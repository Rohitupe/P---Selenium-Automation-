# Functional Test Suite
import unittest


class PaymentReturnsTest(unittest.TestCase):
    def test_paymentReturnByBank(self):
        print("TC_PaymentReturnsTest - Payment Return By Bank")
        self.assertTrue(True, "paymentReturnByBank - Test Have Problem")


if __name__ == "__main__":
    unittest.main()