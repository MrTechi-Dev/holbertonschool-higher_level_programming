#!/usr/bin/python3
"""This is a class Rectangle  defined by width"""


class Rectangle:
    """Definition of attributes"""
    def __init__(self, width=0, height=0):
        """The __init__ method of the class
        Args:
            width(int): Private attribute default 0
            height(int): Private attribute default 0
        Raises:
            TypeError:
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute."""
        return self.__width

    @property
    def height(self):
        """Private instance attribute."""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise valueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """The perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """use the # to make a rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")
        hashtag = (("#" * self.__width + "\n") * self.height)[:-1]
        return hashtag

    def __repr__(self):
        """returns the a representation of the self object"""
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """is usually called when the instance is about to be destriyed"""
        print("Bye rectangle...")
