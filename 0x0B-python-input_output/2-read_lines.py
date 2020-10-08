#!/usr/bin/python3
import os
"""
Basic file reading
"""


def read_lines(filename="", nb_lines=0):
    """reads n number of lines from the .txt file"""
    with open("my_file_0.txt", 'r', encoding="utf-8") as myFile:
        if nb_lines <= 0:
            file = myFile.readlines()
            for i in file:
                print(i, end='')

        else:
            file = myFile.readlines()[0:nb_lines]
            for i in file:
                print(i, end='')
