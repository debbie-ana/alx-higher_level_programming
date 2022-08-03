#!/usr/bin/python3
"""JSON representation module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a textfile,
    using a JSON representation"""
    obj = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(obj)
