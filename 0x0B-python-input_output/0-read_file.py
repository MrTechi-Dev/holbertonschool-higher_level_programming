#!/usr/bin/python3
"""
Basic file reading
"""


def read_file(filename=""):
    """
    Function to read a file and print it out
    """
    f = open(filename, 'r')
    for line in f:
        print('{}'.format(line), end='')
