#!/usr/bin/python3
"""First Class Base"""

import json
import csv


class Base:
    """Init Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor initilization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

