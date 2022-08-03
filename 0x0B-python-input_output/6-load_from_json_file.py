#!/usr/bin/python3
"""create object from JSON file"""
import json


def load_from_json_file(filename):
    """this function creates an object from a JSON file"""
    with open(filename) as f:
        json_obj = json.loads(f)
        return json_obj
