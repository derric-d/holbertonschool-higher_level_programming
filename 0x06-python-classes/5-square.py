#!/usr/bin/python3
"""docstr"""


class Square:
    """docstr"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if isinstance(val, int) is False:
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
