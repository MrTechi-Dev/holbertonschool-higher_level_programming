#!/usr/bin/python3
""" Python module  """


def find_peak(list_of_integers):
    """ Function to find a peak """
    if not len(list_of_integers):
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
