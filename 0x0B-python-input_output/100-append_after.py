#!/usr/bin/python3
"""append after wordgiven"""


def append_after(fn="", s_s="", n_s=""):
    """func"""
    with open(fn, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(fn, 'w', encoding='utf-8') as file:
        for line in lines:
            if s_s in line:
                line += n_s
            file.write(line)
