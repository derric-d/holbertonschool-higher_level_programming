#!/usr/bin/python3
"""doc"""


class Student:
    """doc"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """json"""
        return self.__dict__
