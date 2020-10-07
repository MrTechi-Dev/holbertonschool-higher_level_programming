#!/usr/bin/python3
""" lookup method """


class MyInt(int):
    '''inverted'''
    def __init__(self, size):
        self.__size = size

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
