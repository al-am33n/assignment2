import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import torch
from tensor_multiplication import calculate_matrix_prod_with_bias, calculate_activation, calculate_output, create_tensor_of_val, calculate_elementwise_product, calculate_matrix_product

class TestTensorMultiplication(unittest.TestCase):

    def test_tensor_creation(self):
        res = create_tensor_of_val((2, 3), 3)
        self.assertEqual(res.shape, (2, 3))
        self.assertEqual(res.tolist(), [[3.0, 3.0, 3.0], [3.0, 3.0, 3.0]])
        self.assertIsInstance(res, torch.Tensor)

    def test_elementwise_product(self):
        A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        B = torch.tensor([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])
        self.assertEqual(calculate_elementwise_product(A, B).tolist(), [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])
        self.assertIsInstance(calculate_elementwise_product(A, B), torch.Tensor)

    def test_elementwise_product_fails(self):
        A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        B = torch.tensor([0.5, 0.5, 0.5, 1.0])
        with self.assertRaises(RuntimeError):
            calculate_elementwise_product(A, B)

if __name__ == '__main__':
    unittest.main()

