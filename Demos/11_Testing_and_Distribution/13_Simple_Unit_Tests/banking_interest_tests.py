import unittest
from banking_logic import deposit, withdraw

class TestInterestCalculations(unittest.TestCase):
    # for brevity of demo these are the same tests as in the banking_logic_tests file
    # They do NOT test for any kind of interest being applied

    def test_deposit_increases_balance(self):
        result = deposit(100, 50)
        self.assertEqual(result, 150)

    def test_deposit_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            deposit(100, -10)

    def test_withdraw_reduces_balance(self):
        result = withdraw(100, 40)
        self.assertEqual(result, 60)

    def test_withdraw_too_much_raises_error(self):
        with self.assertRaises(ValueError):
            withdraw(100, 200)

    def test_withdraw_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            withdraw(100, -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)