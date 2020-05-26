#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """welcome to class"""
    def __init__(self, width=0, height=0):
        """doc"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """doc"""
        return self.__width

    @width.setter
    def width(self, val):
        """doc"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """doc"""
        return self.__height

    @height.setter
    def height(self, val):
        """doc"""
        if type(val) != int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be >= 0")
        self.__height = val
