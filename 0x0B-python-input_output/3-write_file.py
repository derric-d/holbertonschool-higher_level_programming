#!/usr/bin/python3
"""doc"""


def write_file(fn="", text=""):
    """doc"""

    with open(fn, 'w', encoding='utf-8') as file:
        res = file.write(text)
    return res
