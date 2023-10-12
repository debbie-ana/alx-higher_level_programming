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
        reload_from_json: replaces all attributes of the student instance
    """

    def __init__(self, first_name, last_name, age):
        """instance method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student instance"""
        if attrs is not None:
            drep = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return drep
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
