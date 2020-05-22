#!/usr/bin/python3
"""Add a and b
a: int/float
b: int/float
return: sum of a and b
"""


def add_integer(a, b=98):
    """a: int
    b: int
    return: a + b """

    if a is None or (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
