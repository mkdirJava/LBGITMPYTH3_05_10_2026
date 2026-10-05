import unittest
from test_bank_transactions import TestBankTransactions

def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(
        TestBankTransactions("test_deposit_increases_balance")
    )
    test_suite.addTest(
        TestBankTransactions("test_deposit_negative_amount_raises_error")
    )
    test_suite.addTest(
        TestBankTransactions("test_withdraw_reduces_balance")
    )
    test_suite.addTest(
        TestBankTransactions("test_withdraw_too_much_raises_error")
    )
    test_suite.addTest(
        TestBankTransactions("test_withdraw_negative_amount_raises_error")
    )

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())