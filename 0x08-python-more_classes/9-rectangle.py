#!/usr/bin/python3
"""This is a class Rectangle  defined by width"""


class Rectangle:
    """Definition of attributes"""
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
        ashtag = ((str(self.print_symbol) * self.__width + "\n") * self.height)
        ashtag = ashtag[:-1]
        return ashtag

    def __repr__(self):
        """returns the a representation of the self object"""
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """is usually called when the instance is about to be destriyed"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a  very new Rectangle instance with
        width == height == size"""
        return cls(size, size)
