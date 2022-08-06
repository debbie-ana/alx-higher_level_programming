#!/usr/bin/python3
The ``2-matrix_divided`` module 
 ====================== 
  
Using ``matrix_divided``
----------------------------------------------
Checking for module docstring:
    >>> md = __import__("2-matrix_divided").__doc__
    >>> len(md) > 1
    True

Importing the function from the module:
    >>> matrix_divided = __import__("2-matrix_divided").matrix_divided

Checking for function docstring:
    >>> fd = __import__("2-matrix_divided").matrix_divided.__doc__
    >>> len(fd) > 1
    True

Regular test:
    >>> matrix = [[4, 6, 8], [2, 9, 3]]
    >>> print(matrix_divided(matrix, 2))
    [[2.0, 3.0, 4.0], [1.0, 4.5, 1.5]]
    >>> print(matrix)
    [[4, 6, 8], [2, 9, 3]]
