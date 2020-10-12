#!/usr/bin/python3
"""Second class Square"""
from models.rectangle import Rectangle
"""import the class rectangle.py"""


class Square(Rectangle):
    """class Square that inherit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Contructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getters size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def update(self, *x, **z):
        """Updating variable arguments"""
        j = ['id', 'size', 'x', 'y']
        i = 0
        if z:
            for key, value in z.items():
                setattr(self, key, value)
                i += 1
        if x:
            for c in x:
                setattr(self, j[i], c)
                i += 1

    def to_dictionary(self):
        """dictionary of square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
