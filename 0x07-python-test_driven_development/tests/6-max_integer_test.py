#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_int = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_base(self):
        self.assertEqual(max_int([1, 2, 3, 4]), 4)
        self.assertEqual(max_int([-10, 2, 0, 6]), 6)
        self.assertEqual(max_int([1]), 1)
        self.assertEqual(max_int([-1, -2, -3, -4]), -1)

    def test_types_in_list(self):
        self.assertEqual(max_int("abc"), "c")
        self.assertEqual(max_int([1.1, 1.2, 1.21]), 1.21)

    def test_multitypes(self):
        self.assertEqual(max_int([1, 2.1, 2]), 2.1)

        with self.assertRaises(TypeError):
            max_int(1)
        with self. assertRaises(TypeError):
            max_int([1, "2", 3])

    def test_none(self):
        self.assertIsNone(max_int([]))
