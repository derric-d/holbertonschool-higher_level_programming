#!/usr/bin/python3
"""doc"""
from json import load


def load_from_json_file(fn):
    """doc"""

    with open(fn, 'r', encoding='utf-8') as file:
        text = load(file)
    return text
