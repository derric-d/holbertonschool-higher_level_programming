#!/usr/bin/python3
"""doc"""
from json import dumps


def save_to_json_file(my_obj, fn):
    """doc"""

    with open(fn, 'w', encoding='utf-8') as file:
        text = dumps(my_obj)
        file.write(text)
