import unittest
from io import StringIO
import sys
from bank_utils import print_account_summary

class TestAccountSummary(unittest.TestCase):
# A common challenge in testing is handling output to stdout.
# The solution is to use a StringIO file handle:
    def setUp(self):
        self._stdout = sys.stdout
        # Redirect stdout to a StringIO object
        self.captured_output = StringIO()
        sys.stdout = self.captured_output


    def test_print_account_summary(self):
        # Call the function
        print_account_summary("ACC1001", 1234.5)

        # Get output and test it
        output = self.captured_output.getvalue().strip()
        expected = "ACC1001 has a balance of £1234.50"

        self.assertEqual(output, expected)

def tearDown(self):
    sys.stdout = self._stdout

if __name__ == "__main__":
    unittest.main(verbosity=2)