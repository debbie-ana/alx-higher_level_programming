#!/usr/bin/python3
"""matrix module"""


def matrix_divided(matrix, div):
    """returns a new matrix after dividing
    each elements in the matrix"""
    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for a in row:
            if type(a) is not int and type(a) is not float:
                raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(a / div, 2) for a in row] for row in matrix]
