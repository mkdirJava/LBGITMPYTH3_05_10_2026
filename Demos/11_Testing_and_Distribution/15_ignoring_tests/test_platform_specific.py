import unittest
import sys

class TestPlatformSpecific(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires Windows")
    def test_windows_only_feature(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.version_info >= (3, 10), "Requires Python 3.10+")
    def test_modern_python_feature(self):
        self.assertEqual((1, 2, 3), tuple([1, 2, 3]))

if __name__ == "__main__":
    unittest.main(verbosity=2)