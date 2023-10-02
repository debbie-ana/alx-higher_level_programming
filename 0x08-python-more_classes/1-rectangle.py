#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ a rectangle class"""

    def __init__(self, width=0, height=0):
        """initialization of the class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width
        Args:
            value (int): value for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height
        Returns:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height
        Args:
            value (int): value for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
