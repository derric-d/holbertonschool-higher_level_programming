#!/usr/bin/python3
"""
matrix-divided:
divide matrix elements
"""


def matrix_divided(matrix, div):
    """divide matrix members"""
    mtx_te = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(mtx_te)

    try:
        lenlst = len(matrix[0])
    except TypeError:
        raise TypeError(mtx_te)

    ret_mtx = []

    for inmtx in matrix:
        if not isinstance(inmtx, list):
            raise TypeError(mtx_te)
        elif len(inmtx) != lenlst:
            raise TypeError("Each row of the matrix must have the same size")
       # new_inmtx = []
        for num in inmtx:
            if not isinstance(num, (int, float)):
                raise TypeError(mtx_te)
         #   new_inmtx.append(round(num/div, 2))
        #ret_mtx.append(new_inmtx)
    return [[round(num/div, 2) for num in inmtx] for inmtx in matrix]

