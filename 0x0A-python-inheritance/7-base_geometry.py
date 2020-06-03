#!/usr/bin/python3
"""base geo"""


class BaseGeometry(object):
    """class basegeo"""

    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check ints"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
