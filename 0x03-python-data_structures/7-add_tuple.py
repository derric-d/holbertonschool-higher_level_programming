#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ele1 = tuple_a + (0, 0)
    ele2 = tuple_b + (0, 0)
    return (ele1[0] + ele2[0], ele1[1] + ele2[1])
