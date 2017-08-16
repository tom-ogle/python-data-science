import unittest
from unittest import TestCase

from linear_algebra.matrices import shape, get_row, get_column, make_matrix, indentity_matrix


class TestMatrices(TestCase):

    def test_shape(self):
        matrix = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ]
        num_rows, num_cols = shape(matrix)
        self.assertEqual(4, num_rows)
        self.assertEqual(3, num_cols)

    def test_shape_empty_rows(self):
        matrix = [
            [],
            [],
            [],
            []
        ]
        num_rows, num_cols = shape(matrix)
        self.assertEqual(4, num_rows)
        self.assertEqual(0, num_cols)

    def test_shape_no_columns(self):
        matrix = []
        num_rows, num_cols = shape(matrix)
        self.assertEqual(0, num_rows)
        self.assertEqual(0, num_cols)

    def test_get_row(self):
        matrix = [
            [1, 2, 3],
            ['a', 'b', 'c'],
            [3, 2, 1],
            ['x', 'y', 'z']
        ]
        row = get_row(matrix, 1)
        self.assertEqual(['a', 'b', 'c'], row)

    def test_get_column(self):
        matrix = [
            [1, 2, 3],
            ['a', 'b', 'c'],
            [3, 2, 1],
            ['x', 'y', 'z']
        ]
        column = get_column(matrix, 2)
        self.assertEqual([3, 'c', 1, 'z'], column)

    def test_make_matrix(self):
        expected_result = [
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        result = make_matrix(2, 4, lambda i, j: 1)
        self.assertEqual(expected_result, result)

    def test_identity_matrix(self):
        expected_result = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        result = indentity_matrix(3, 3)
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()