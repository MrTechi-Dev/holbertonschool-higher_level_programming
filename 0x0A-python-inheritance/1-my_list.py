#!/usr/bin/python3


class MyList(list):
    """class that inherit from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
