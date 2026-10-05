import unittest
from banking_logic_tests import TestBankTransactions

def suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(TestBankTransactions)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())