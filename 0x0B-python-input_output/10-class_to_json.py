#!/usr/bin/python3
"""doc"""


def class_to_json(obj):
    """json"""

    if hasattr(obj, '__dict__'):
        return obj.__dict__
