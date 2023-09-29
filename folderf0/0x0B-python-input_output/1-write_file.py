#!/usr/bin/python3

"""file writing module"""


def write_file(filename="", text=""):
    """this function writes text to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
