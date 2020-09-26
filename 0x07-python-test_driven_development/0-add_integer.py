#!/usr/bin/python3
""" Add method """


def add_integer(a, b=98):
    """ Method that add two integers of floats
    Args:
        a (int or float): first parameter
        b (int or float): second parameter
    Raises:
        TypeError: If first parameter or second parameter are
        not integers or floats
    Returns:
        the two parameters add result
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
