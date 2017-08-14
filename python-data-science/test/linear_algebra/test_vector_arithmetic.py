import unittest
from unittest import TestCase

from linear_algebra.vector_arithmetic import vector_add, vector_subtract, vector_sum, scalar_multiply, vector_mean, \
    dot_product, sum_of_squares, magnitude, distance


class TestVectorArithmetic(TestCase):

    def test_vector_add(self):
        v = [1, 2, 3]
        w = [10, 9, 8]
        result = vector_add(v, w)
        expected_result = [11, 11, 11]
        self.assertEqual(result, expected_result)

    def test_vector_subtract(self):
        v = [10, 9, 8]
        w = [3, 4, 5]
        result = vector_subtract(v, w)
        expected_result = [7, 5, 3]
        self.assertEqual(result, expected_result)

    def test_vector_sum(self):
        vectors = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6]
        ]
        result = vector_sum(vectors)
        expected_result = [6, 9, 12, 15]
        self.assertEqual(result, expected_result)

    def test_scalar_multiply(self):
        c = 10
        v = [10, 9, 8]
        result = scalar_multiply(c, v)
        expected_result = [100, 90, 80]
        self.assertEqual(result, expected_result)

    def test_vector_mean(self):
        vectors = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6]
        ]
        result = vector_mean(vectors)
        expected_result = [2, 3, 4, 5]
        self.assertEqual(result, expected_result)

    def test_dot_product(self):
        v = [2, 3, 4]
        w = [1, 2, 3]
        result = dot_product(v, w)
        expected_result = 20
        self.assertEqual(result, expected_result)

    def test_sum_of_squares(self):
        v = [1, 3, 5]
        result = sum_of_squares(v)
        expected_result = 35
        self.assertEqual(result, expected_result)

    def test_magnitude(self):
        v = [1, 3, 5, 1]
        result = magnitude(v)
        expected_result = 6
        self.assertEqual(result, expected_result)

    def test_distance(self):
        v = [2, 3, 5, 6]
        w = [1, 1, 2, 3]
        result = distance(v, w)
        expected_result = 3
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()