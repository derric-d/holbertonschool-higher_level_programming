#!/usr/bin/python3
"""my_int"""


class MyInt(int):
    """class"""

    def __eq__(self, other):
        """set eq opposite(__ne__)"""
        return int(self) != int(other)

    def __ne__(self, other):
        """set ne opposite(__eq__)"""
        return int(self) == int(other)
