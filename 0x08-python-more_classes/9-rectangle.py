#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """welcome to class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """doc"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """doc"""
        return (self.__width * self.__height)

    def perimeter(self):
        """doc"""
        if 0 in (self.__width, self.__height):
            return (0)
        else:
            sides = (self.__width + self.__width)
            tottom = (self.__height + self.__height)
            return (sides + tottom)

    def __str__(self):
        """doc"""
        if 0 in (self.__width, self.__height):
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + "\n") *
                    self.__height)

    def __repr__(self):
        """doc"""
        reprstr = ("{}({}, {})".format(self.__class__.__name__,
                                       self.width, self.height))
        return (reprstr)

    def __del__(self):
        """doc"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """doc"""
        if type(rect_1) != Rectangle:
            raise TypeError()
        if type(rect_1) != Rectangle:
            raise TypeError()
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_1

    @classmethod
    def square(cls, size=0):
        """doc"""
        return cls(size, size)
