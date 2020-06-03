#!/usr/bin/python3
"""doc"""


class Student:
    """doc"""

    def __init__(self, first_name, last_name, age):
        """doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        if attrs is None:
            return self.__dict__
        dic = {}
        if type(attrs) == list:
            for item in attrs:
                if type(item) == str:
                    if item in self.__dict__:
                        dic[item] = self.__dict__[item]
            return dic
