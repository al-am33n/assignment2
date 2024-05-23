import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rmse import rmse

class TestRMSE(unittest.TestCase):
    def test_rmse(self):
        predictions = [1, 2, 3, 4, 5]
        targets = [1, 2, 3, 4, 5]
        self.assertEqual(rmse(predictions, targets), 0)

        predictions = [2, 3, 4, 5, 6]
        targets = [1, 2, 3, 4, 5]
        self.assertEqual(rmse(predictions, targets), 1)

if __name__ == '__main__':
    unittest.main()

