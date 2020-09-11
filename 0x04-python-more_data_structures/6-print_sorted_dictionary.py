#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = []
    for x in sorted(set(a_dictionary)):
        print("{}: {}".format(x, a_dictionary[x]))
