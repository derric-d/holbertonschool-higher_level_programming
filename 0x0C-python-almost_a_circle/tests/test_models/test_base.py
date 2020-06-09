#!/usr/bin/python3
"""test for base class"""
import unittest
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """test base"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        new_base = Base()
        self.assertEqual(type(new_base), Base)

    def test_id(self):
        new = Base()
        self.assertEqual(new.id, 1)
        new2 = Base(42)
        self.assertEqual(new2.id, 42)

    def test_to_json_string(self):
        rec = Rectangle(9, 8, 3, 5)
        dic = rec.to_dictionary()
        json_d = Base.to_json_string([dic])
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(json_d), str)
        tmp = []
        self.assertEqual(Base.to_json_string(tmp), "[]")
        self.assertEqual(type(dic), dict)

    def test_save_to_file(self):
        rec = Rectangle(9, 8, 3, 5)
        rec2 = Rectangle(7, 3)
        Rectangle.save_to_file([rec, rec2])
        frm_file = []
        with open("Rectangle.json", "r") as file:
            frm_file = json.loads(file.read())
        lst_d = [rec.to_dictionary(), rec2.to_dictionary()]
        self.assertEqual(lst_d, frm_file)

    def test_from_json(self):
        lst = [
            {'id': 21, 'width': 12, 'height': 6},
            {'id': 12, 'widht': 21, 'height': 11}
        ]
        json_lst = Rectangle.to_json_string(lst)
        json_out = Rectangle.from_json_string(json_lst)
        self.assertEqual(type(lst), list)
        self.assertEqual(type(json_lst), str)
        self.assertEqual(type(json_out), list)
        self.assertEqual(lst, json_out)

    def test_create(self):
        rec = Rectangle(9, 8, 3, 5)
        rec_d = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_d)
        self.assertEqual(str(rec), str(rec2))
        self.assertNotEqual(rec, rec2)

    def test_load_from_file(self):
        try:
            os.remove('Rectangle.json')
        except:
            pass
        rec = Rectangle(9, 8, 3, 5)
        rec2 = Rectangle(10, 5)
        lst = [rec, rec2]
        Rectangle.save_to_file(lst)
        lst_out = Rectangle.load_from_file()
        self.assertEqual(str(lst[0]), str(lst_out[0]))
        self.assertEqual(str(lst[1]), str(lst_out[1]))
