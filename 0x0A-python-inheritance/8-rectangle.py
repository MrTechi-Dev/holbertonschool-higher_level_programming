#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" lookup method """


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
