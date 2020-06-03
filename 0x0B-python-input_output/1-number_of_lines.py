#!/usr/bin/python3
"""doc"""


def number_of_lines(filename=""):
    """doc"""

    num = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            num += 1

    return num
