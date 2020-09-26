#!/usr/bin/python3
"""This module defines the text_indentation function"""


def text_indentation(text):
    """Function that indent a text
    Arguments:
        text {string} -- Texto to be indented
    Raises:
        TypeError: text must be a string
    """
    temp_text = ''
    if type(text) != str:
        raise TypeError("text must be a string")

    for character in text:
        temp_text += character
        if character in ['?', '.', ':']:
            print(temp_text.strip() + "\n")
            temp_text = ''
    print(temp_text.strip(), end="")
