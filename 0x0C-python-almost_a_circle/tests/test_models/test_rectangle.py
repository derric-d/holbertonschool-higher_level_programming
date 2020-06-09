#!/usr/bin/python3
"""testrec"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """test rect"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_assignments(self):
        rec = Rectangle(12, 3, 4, 5, 3)
        self.assertEqual(rec.id, 3)
        self.assertEqual(rec.width, 12)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)

    def test_display(self):
        new = io.StringIO()
        str_out = ('#' * 5 + '\n') * 5
        rec = Rectangle(5, 5)
        with redirect_stdout(new):
            rec.display()
        self.assertEqual(new.getvalue(), str_out)

    def test_update(self):
        sq = Rectangle(1, 1, 1, 1)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.width, 1)
        self.assertEqual(sq.height, 1)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 1)
        sq.update(2)
        self.assertEqual(sq.id, 2)
        sq.update(id=3, width=2, height=2, x=2, y=2)
        self.assertEqual(sq.id, 3)
        self.assertEqual(sq.width, 2)
        self.assertEqual(sq.height, 2)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 2)
        sq.update(width=100)
        self.assertEqual(sq.width, 100)

    def test_validation(self):
        sq = Rectangle(5, 5)
        self.assertEqual(str(sq), '[Rectangle] (1) 0/0 - 5/5')
        sq.width = 6
        self.assertEqual(str(sq), '[Rectangle] (1) 0/0 - 6/5')
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            sq.width = "6"
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            sq.width = -1

    def test_area(self):
        rec = Rectangle(5, 5)
        self.assertEqual(rec.area(), 25)
