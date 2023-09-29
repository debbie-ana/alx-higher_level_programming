#!/usr/bin/python3
"""module for JSON
JavaScript Object Notation representation"""
import json


def from_json_string(my_obj):
    """returns an object(python data structure)
    represented by a JSON string"""
    return json.loads(my_obj)
