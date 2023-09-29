#!/usr/bin/python3
"""print square module"""


def print_square(size):
    """this function prints a square
    given the size length of the square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        print("".join(["#" for b in range(size)]))
