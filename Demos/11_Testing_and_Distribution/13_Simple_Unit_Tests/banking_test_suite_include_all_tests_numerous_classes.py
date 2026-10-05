import unittest
from banking_logic_tests import TestBankTransactions
from banking_interest_tests import TestInterestCalculations

def suite():
    loader = unittest.TestLoader()

    test_suite = unittest.TestSuite([
        loader.loadTestsFromTestCase(TestBankTransactions),
        loader.loadTestsFromTestCase(TestInterestCalculations)
    ])

    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())