#!/usr/bin/python3
"""
Basic file number lines
"""


def number_of_lines(filename=""):
    """return number of lones of a text file"""
    with open(filename, encoding="utf-8") as myFile:
        readmyFile = len(myFile.readlines())
        return readmyFile
