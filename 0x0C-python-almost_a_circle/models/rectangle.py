#!/usr/bin/python3
"""Rectangle module"""
from base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization class"""
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width value"""
        self.__width = width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height value"""
        self.__height = height

    @property
    def x(self):
        """returns value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the value of x"""
        self.__x = x

    @property
    def y(self):
        """returns value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the value of y"""
        self.__y = y
