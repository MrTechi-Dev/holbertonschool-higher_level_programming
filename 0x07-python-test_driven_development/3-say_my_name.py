#!/usr/bin/python3
""" Add method """


def say_my_name(first_name, last_name=""):
    """ Method that print the name#
    Args:
        First_name(string): name.
        last_name(string): last name
        Raises:
        TypeError: If parameter is not a String
    Returns:
        A printed full name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
