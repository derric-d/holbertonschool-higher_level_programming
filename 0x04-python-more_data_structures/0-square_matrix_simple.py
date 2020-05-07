#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = map(list, matrix)
    return ([[ele ** 2 for ele in lst] for lst in new])
