#!/usr/bin/python3
""" lookup method """


class BaseGeometry():
    """class"""
    def area(self):
        """ Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area rectangle"""
        return self.__width * self.height

    def __str(self):
        """print string"""
        return ["Rectangle"] + str(self.__width) + "/" + str(self.__height)
