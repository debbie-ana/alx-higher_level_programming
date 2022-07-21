#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a class Square
    Attributes:
        __size (int): length of a side of square
        __position (int tuple): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialisation of class

        Args:
            size (int): length of square
            position (int tuple): position of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """property to retrieve position of square
        Returns:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """property to set position of the square
        Args:
            value (int tuple): position to set square to
        Returns:
            None
        """
        if type(value) == tuple and len(value) == 2:
            if type(value[0]) == int and type(value[1]) == int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be tuple of 2 positive integers")

    def my_print(self):
        """ prints square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for a in range(self.__size):
            print("".join([" " for b in range(self.__position[0])]), end="")
            print("".join(["#" for c in range(self.__size)]))

    def __str__(self):
        """ define print representation of square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
            return ("")
