#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for x in a_dictionary:
        x, new[x] = x, a_dictionary[x] * 2
    return new
