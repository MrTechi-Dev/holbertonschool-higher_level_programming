#!/usr/bin/python3
"""defines a square """


class Square:
    """ class initialization """
    def __init__(self, size=0, position=(0, 0)):
        """ Definition with private instance attribute size
        which is asigned with the double underscore before given name
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        A method used for getting a value is decorated with @property
        """
        return self.__size

    @property
    def position(self):
        """
        A method used for getting a value is decorated with @property
        Returns:
        """
        return self.__position

    @size.setter
    def size(self, value):
        """ size definition to setter the data, now size will be equal to value
        A method that function as the setter is decorated with @ .setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):

        """ size definition to setter the data, now size will be equal to value
        A method that function as the setter is decorated with @ .setter

        """
        if type(value) is not tuple or len(value) is not 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Public instance method
        Returns:
            Square Area. self.size ** 2
        """
        return self.size * self.size

    def my_print(self):
        """ Public instance method that prints in stdout
        the square with the character #
        """
        if self.size is 0:
            print("")
        else:
            for jumps in range(self.position[1]):
                print("")
            for row in range(self.size):
                print(" " * self.position[0], end="")
                for column in range(self.size):
                    print("#", end="")
                print("")
