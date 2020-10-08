#!/usr/bin/python3
"""
Basic file reading
"""


def read_file(filename=""):
    """read the file"""
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        print(myFile.read())
