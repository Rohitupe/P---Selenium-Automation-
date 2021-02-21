import unittest
# Import Package 1
from Practice.TestSuites_Project_21.Package1.TC_LoginTest import LoginTest
from Practice.TestSuites_Project_21.Package1.TC_SignupTest import SignUpTest

# Import Package 2
from Practice.TestSuites_Project_21.Package2.TC_PaymentTest import PaymentTest
from Practice.TestSuites_Project_21.Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get All tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnsTest
loginTest1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
signUpTest2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
paymentTest3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
paymentReturnsTest4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)


# Creating Test Suites

# 1. Sanity Test - Login & Signup
SANITY_TEST_suite = unittest.TestSuite([loginTest1, signUpTest2])  # sanity test suite

# unittest.TextTestRunner().run(SANITY_TEST_suite)  # run sanity test suite

# 2. Functional Test - Payment and Payment Returns
FUNCTIONAL_TEST_suite = unittest.TestSuite([paymentTest3, paymentReturnsTest4])  # functional test suite

# unittest.TextTestRunner().run(FUNCTIONAL_TEST_suite)  # run functional test suite

# 3. Master Test - Run all tests
MASTER_TEST_SUITE = unittest.TestSuite([loginTest1, signUpTest2, paymentTest3, paymentReturnsTest4])  # master test suite

unittest.TextTestRunner(verbosity=2).run(MASTER_TEST_SUITE)  # run all test cases
# verbosity will give some extra logs while running test cases

