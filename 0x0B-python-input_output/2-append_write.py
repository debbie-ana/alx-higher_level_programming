#!/usr/bin/python3
"""file append module"""


def append_write(filename="", text=""):
    """this function appends text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
