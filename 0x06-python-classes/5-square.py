#!/usr/bin/python3


class Square:

    def __init__(self, size=0):

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        return self.__size * self.__size

    def my_print(self):
        if not self.__size:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
