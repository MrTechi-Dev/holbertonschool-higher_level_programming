#!/usr/bin/python3
"""
Class
"""


class Student():
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student Instance"""
        dir1 = vars(self)
        if type(attrs) is list:
            dir2 = {}
            set_dir = set(dir1)
            set_list = set(attrs)
            keys = list(set_dir & set_list)
            for key in keys:
                dir2[key] = dir1[key]
            return (dir2)
        else:
            return dir1
