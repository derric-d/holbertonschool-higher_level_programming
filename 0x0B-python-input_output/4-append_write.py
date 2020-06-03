#!/usr/bin/python3
"""doc"""


def append_write(fn="", text=""):
    """doc"""

    with open(fn, 'a', encoding='utf-8') as file:
        res = file.write(text)
    return res
