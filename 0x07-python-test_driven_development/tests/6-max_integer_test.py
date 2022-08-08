#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max integer function"""
    def test_maxint(self):
        self.assertEqual(max_integer([2, 5, 1]), 5)
        self.assertEqual(max_integer([1, 2, 5, 9]), 9)
        self.assertEqual(max_integer([6, 0, -1]), 6)
        self.assertEqual(max_integer([-2, -5, -10]), -2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-2]), -2)
