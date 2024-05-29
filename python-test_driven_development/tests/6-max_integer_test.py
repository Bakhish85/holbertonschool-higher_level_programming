#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_result(self):
        # Test the function result with correct type of values.
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4, 2, 3, -4]), 4)
        self.assertAlmostEqual(max_integer([1.2, 12.3, 4, -5.7]), 12.3)
        self.assertAlmostEqual(max_integer([]), None)

    def test_values(self):
        # Test if the argument of function is list.
        self.assertRaises(ValueError, max_integer, [1, 2, '3', 4])
