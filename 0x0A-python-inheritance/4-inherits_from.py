#!/usr/bin/python3
"""check inheritance"""


def inherits_from(obj, a_class):
    """inheritance"""

    return (isinstance(obj, a_class) and type(obj) is not a_class)
