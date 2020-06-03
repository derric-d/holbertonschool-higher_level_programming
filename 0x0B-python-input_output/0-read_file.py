#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
