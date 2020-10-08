#!/usr/bin/python3
import os


def append_write(filename="", text=""):
    """ write a new file and count number of chars"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
