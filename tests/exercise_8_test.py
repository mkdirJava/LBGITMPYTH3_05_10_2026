import unittest
from work.exercise_8 import PostCodeLookUp



class PostCodeClientTest(unittest.TestSuite):

    def test_successful():
        unit = PostCodeLookUp()
        unit.call("BS15 4XX")
