#!/usr/bin/python3


class Square:
    """Inizialitation class"""
    def __init__(self, size=0):
        """The initialization method of the square class
        Args:
            size (int): Is the type int private attribute
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
