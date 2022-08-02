#!/usr/bin/python3

"""file reading module"""


def read_file(filename=""):
    """this function reads a file
    and prints to standard output"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
