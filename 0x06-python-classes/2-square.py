#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a class Square
    Attributes:
        __size (int): length of a side of square
    """

    def __init__(self, size=0):
        """Initialisation of class

        Args:
            size (int): length of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
