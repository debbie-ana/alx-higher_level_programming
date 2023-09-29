#!/usr/bin/python3
"""student to json"""


class Student:
    """
    defines a student
    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    Methods:
        __init__: initialization method
        to_json: gets dictionary representation of instance
    """

    def __init__(self, first_name, last_name, age):
        """instance method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student instance"""
        return self.__dict__
