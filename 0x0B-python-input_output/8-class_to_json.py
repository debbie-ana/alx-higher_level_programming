#!/usr/bin/python3
"""module for class to json"""


def class_to_json(obj):
    """this function returns a dictionary description
    witn simple data structure for JSON serialization of an object"""
    return obj.__dict__
