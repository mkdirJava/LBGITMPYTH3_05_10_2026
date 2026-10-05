import unittest
from bank_utils import calc_daily_interest

class TestCalcDailyInterest(unittest.TestCase):

    def setUp(self):
        self.accounts = {
            "ACC1": {
                "opening_balance": 1000.0,
                "interest_rate": 0.0365,  # makes daily interest easy (0.0001)
                "transactions_by_day": {
                    0: [{"amount": 100.0}],
                    1: [{"amount": -50.0}]
                }
            }
        }

    def test_basic_interest_calculation(self):
        result = calc_daily_interest(self.accounts, 2)
        self.assertIn("ACC1", result)
        self.assertGreater(result["ACC1"], 1000.0)

    def test_no_transactions(self):
        accounts = {
            "ACC2": {
                "opening_balance": 1000.0,
                "interest_rate": 0.0365,
                "transactions_by_day": {}
            }
        }
        result = calc_daily_interest(accounts, 2)
        self.assertGreater(result["ACC2"], 1000.0)

    def test_negative_transactions(self):
        accounts = {
            "ACC3": {
                "opening_balance": 1000.0,
                "interest_rate": 0.0365,
                "transactions_by_day": {
                    0: [{"amount": -200.0}]
                }
            }
        }
        result = calc_daily_interest(accounts, 1)
        self.assertLess(result["ACC3"], 1000.0)

    def test_multiple_accounts(self):
        accounts = {
            "A": {
                "opening_balance": 1000.0,
                "interest_rate": 0.03,
                "transactions_by_day": {}
            },
            "B": {
                "opening_balance": 2000.0,
                "interest_rate": 0.03,
                "transactions_by_day": {}
            }
        }
        result = calc_daily_interest(accounts, 1)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)