#!/usr/bin/python3
"""
Basic file reading
"""


def read_lines(filename="", nb_lines=0):
    """reads n number of lines from the .txt file"""
    nlines = len(open(filename).readlines())
    with open(filename, encoding="utf-8") as f:
        if nb_lines > 0 and nb_lines < nlines:
            for lines in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
