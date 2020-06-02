#!/usr/bin/python3
"""doc"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rec"""

    def __init__(self, width, height):
        """init"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """get area"""
        return self.__width * self.__height

    def __str__(self):
        """rep str"""
        w = str(self.__width)
        h = str(self.__height)
        return "[Rectangle] " + w + "/" + h
