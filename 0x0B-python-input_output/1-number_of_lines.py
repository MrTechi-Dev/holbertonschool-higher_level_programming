#!/usr/bin/python3
import os
"""
Basic file number lines
"""


def number_of_lines(filename=""):
    """returnd number of lones of a text file"""
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        readmyFile = len(myFile.readlines())
        return readmyFile
