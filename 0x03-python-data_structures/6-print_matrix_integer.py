#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for line in matrix:
        if len(line) == 0:
            print()
        for idx, ele in enumerate(line):
            print("{:d}".format(line[idx]),
                  end="\n" if idx == len(line) - 1 else " ")
