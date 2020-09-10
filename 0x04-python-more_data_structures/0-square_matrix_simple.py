#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newone = matrix.copy()
    for i in range(len(newone)):
        newone[i] = list(map(lambda num: num ** 2, newone[i]))
    return newone
