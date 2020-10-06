#!/usr/bin/python3
""" lookup method """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size

    def str(self):
        """print statement"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
