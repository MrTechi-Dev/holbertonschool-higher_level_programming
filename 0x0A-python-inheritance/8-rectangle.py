#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


    def area(self):
        """area rectangle"""
        return self.__width * self.height


    def __str(self):
        """print string"""
        return ["Rectangle"] + str(self.__width) + "/" + str(self.__height)
