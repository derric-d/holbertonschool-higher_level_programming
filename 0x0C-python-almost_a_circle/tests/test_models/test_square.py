#!/usr/bin/python3
"""testSquare"""
import unittest
import json
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_Square(unittest.TestCase):
    """testsquare"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str(self):
        sq = Square(12, 3, 4, 5)
        sq2 = Square(5)
        self.assertEqual(str(sq), '[Square] (5) 3/4 - 12')
        self.assertEqual(str(sq2), '[Square] (1) 0/0 - 5')

    def test_validation(self):
        sq = Square(5)
        self.assertEqual(str(sq), '[Square] (1) 0/0 - 5')
        sq.size = 6
        self.assertEqual(str(sq), '[Square] (1) 0/0 - 6')
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            sq.size = "6"
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            sq.size = -1

    def test_dictionary(self):
        sq = Square(12, 3, 4)
        sq_d = sq.to_dictionary()
        self.assertEqual(sq_d, {'id': 1, 'size': 12, 'x': 3, 'y': 4})
        self.assertEqual(type(sq_d), dict)

    def test_update(self):
        sq = Square(1, 1, 1)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 1)
        sq.update(2)
        self.assertEqual(sq.id, 2)
        sq.update(id=3, size=2, x=2, y=2)
        self.assertEqual(sq.id, 3)
        self.assertEqual(sq.size, 2)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 2)
        sq.update(size=100)
        self.assertEqual(sq.size, 100)

if __name__ == '__main__':
    unittest.main()
