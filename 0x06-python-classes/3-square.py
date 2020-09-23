#!/usr/bin/python3
"""This is a class Square defined by size."""


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

    def size(self):

        """The area public instance method of the square class
        Return:
            The square area
        """
        return self._size

    def area(self):

        return self.__size * self.__size
