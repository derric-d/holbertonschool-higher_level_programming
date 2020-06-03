#!/usr/bin/python3
"""doc"""


def read_lines(filename="", nb_lines=0):
    """read lines"""

    lines = 0
    if nb_lines <= 0:
        lines = -1
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
            if lines != -1:
                lines += 1
                if lines == nb_lines:
                    break
