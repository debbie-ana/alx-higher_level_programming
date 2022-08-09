#!/usr/bin/python3
"""module contains the class Base"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialization method of base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
