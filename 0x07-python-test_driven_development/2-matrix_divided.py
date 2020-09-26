#!/usr/bin/python3
""" Add method """


def matrix_divided(matrix, div):
    """ Method that divided all elemnets of matrix
    Args:
        matrix (int or float): list of integers or float
        div (int or float): second parameter
    Raises:
        TypeError: If first parameter or second parameter are
        not integers or floats
    Returns:
        A new Matrix
    """
    new_matrix = []

    error = "matrix must be a matrix (list of lists) of integers/floats"
    error_l = "Each row of the matrix must have the same size"

    if type(matrix) is not list or matrix == []:
        raise TyprError("error")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        longitude = len(matrix[0])

    for f_matrix in matrix:
        if any(type(x) not in [int, float] for x in f_matrix):
            raise TypeError(error)
        if type(f_matrix) is not list or f_matrix == []:
            raise TypeError(error)
        if len(f_matrix) is not longitude:
            raise TypeError(error_l)
        new_matrix.append(list(map(lambda x: round(x / div, 2), f_matrix)))

    return new_matrix
