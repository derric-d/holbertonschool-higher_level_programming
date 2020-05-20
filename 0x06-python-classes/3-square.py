#!/usr/bin/python3
"""docstr"""


class Square:
    """docstr"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2