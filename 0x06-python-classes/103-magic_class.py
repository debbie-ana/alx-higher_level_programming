#!/usr/bin/python3
"""magic class"""


import math


class MagicClass:
    """class for circle"""

    def __init__(self, radius=0):
        """Initializing the class
        Arg:
            radius (float or int): radius for the class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area for the magic class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference of circle"""
        return (2 * math.pi * self.__radius)
