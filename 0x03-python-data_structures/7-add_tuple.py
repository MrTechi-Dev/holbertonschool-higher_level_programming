#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    res = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return res
