#!/usr/bin/python3
"""module for integer addition
contains function add_integer
"""


def add_integer(a, b=98):
    """returns the addition of 2 integers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
