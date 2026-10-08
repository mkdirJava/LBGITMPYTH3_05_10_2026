import unittest
from work.exercise_8 import PostCodeLookUp



class TestPostCodeClient(unittest.TestCase):

    def test_successful(self):
        unit = PostCodeLookUp()
        unit.call("BS15 4XX")
 