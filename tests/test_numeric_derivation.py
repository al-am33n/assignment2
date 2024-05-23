import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from numeric_derivation import derivative

class TestNumericDerivation(unittest.TestCase):
    def test_derivative(self):
        f = lambda x: x**2
        self.assertAlmostEqual(derivative(f, 1), 2, places=5)

if __name__ == '__main__':
    unittest.main()

