import unittest

from work.exercise_10 import PlayProcessExecutor, TransactionNumberParallel


class TestExercise_10(unittest.TestCase):

    def test_PlayProcessExecutor(self):
        unit = PlayProcessExecutor()
        self.assertEqual(unit.do_something(),"This is a greeting Bob")

    def test_play_executore_shared_memory(self):
        unit = PlayProcessExecutor()
        result = unit.do_somthing_shared()
        self.assertEqual(result["done"],"done")
        
    def test_TransactionNumberParrelle(self):
        unit = TransactionNumberParallel(worker_count=10,prefix="transaction")
        results = unit.get_transactions()
        self.assertTrue(len(results) == 40)