import unittest

loader = unittest.TestLoader()
suite = loader.discover(".", pattern="unit_tests_for_bank_utils_calc_daily_interest.py")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
