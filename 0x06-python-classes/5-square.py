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

    def area(self):
        """Calculates the area of the square
        Returns:
            Area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter method for size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size
        Args:
            value (int): value for size to be set
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
