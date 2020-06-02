#!/usr/bin/python3
"""add attr"""


def add_attribute(cls, name, value):
    """add attr if possible"""
    if not hasattr(cls, '__dict__') and not hasattr(cls, '__slots__'):
        raise TypeError("can't add new attribute")
    if hasattr(cls, "__slots__") and name not in cls.__slots__:
        raise TypeError("can't add new attribute")

    setattr(cls, name, value)
