#!/usr/bin/python3
""" Add method """


def print_square(size):
    """ Method that print a square #
    Args:
        size(int): size lenght of the square
    Raises:
        TypeError: If parameter is not an integer
    Returns:
        A printed sqaure with #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
