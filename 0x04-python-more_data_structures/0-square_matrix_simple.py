#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[ele ** 2 for ele in lst] for lst in matrix]
    return new
