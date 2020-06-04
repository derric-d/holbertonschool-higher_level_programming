#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """doc"""

    lst = []
    if n <= 0:
        return lst
    # n determines rows
    for ele in range(n):
        tmp = [1]
        if lst:
            # now iterate for each element in each row (columns)
            # print("loop")
            for lel in range(ele):
                # take sum of return list last element so far
                # and the row
                # print("in func")
                # print(lst[-1][lel:lel+2])
                tmp.append(sum(lst[-1][lel:lel+2]))
                # print("tmp:")
                # print(tmp)
        lst.append(tmp)
    return lst
