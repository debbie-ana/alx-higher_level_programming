Test(matrix = list of lists of integers and div = integer):
    >>> matrix = [[4, 6, 8], [2, 9, 3]]
    >>> print(matrix_divided(matrix, 2))
    [[2.0, 3.0, 4.0], [1.0, 4.5, 1.5]]
    >>> print(matrix)
    [[4, 6, 8], [2, 9, 3]]

Test(matrix = list of lists of integers and div = string):
    >>> matrix = [[1, 4, 6], [4, 1, 0]]
    >>> print(matrix_divided(matrix, "free"))
    Traceback (most recent call last):
    ...
    TypeError: div must be a number

Test(div = 0):
    >>> matrix = [[1, 9], [6, 2]]
    >>> print(matrix_divided(matrix, 0))
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

Test(matrix is not list of lists of integers and div = integer):
    >>> matrix = (1, 4, 5)
    >>> print(matrix_divided(matrix, 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Test(matrix = list of lists of integers but not rectangular and div = integer):
    >>> matrix = [[1, 2], [5, 9, 0, 1]]
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

Test(div = float(inf)):
    >>> matrix = [[1, 2], [2, 4]]
    >>> print(matrix_divided(matrix, float('inf')))
    [[0.0, 0.0], [0.0, 0.0]]

Test(matrix has one float(inf):
    >>> matrix = [[5, float('inf')], [0, 1]]
    >>> print(matrix_divided(matrix, 2))
    [[2.5, inf], [0, 0.5]]

Test(matrix has one float(nan):
    >>> matrix = [[2, 3], [2, float('nan')]]
    >>> print(matrix_divided(matrix, 2))
    [[1, 1.5], [1, nan]]

Test(matrix = list of lists of integers with one float(inf)
    and div = float(inf):
    >>> matrix = [[3, 6, 5][float('inf'), 1, 0]]
    >>> print(matrix_divided(matrix, float('inf'))
    [[0.0, 0.0, 0.0], [nan, 0.0, 0.0]]

Test(matrix = list of lists of integers with one float(inf)
    and div = float(nan):
    >>> matrix = [[3, 6, 5][float('inf'), 1, 0]]
    >>> print(matrix_divided(matrix, float('nan'))
    [[nan, nan, nan], [nan, nan, nan]]

Test(matrix = list of lists of integers with one float(nan)
    and div = float(inf):
    >>> matrix = [[3, 6, 5][float('nan'), 1, 0]]
    >>> print(matrix_divided(matrix, float('inf'))
    [[0.0, 0.0, 0.0], [nan, 0.0, 0.0]]

Test(matrix = list of lists of integers with one float(nan)
    and div = float(nan):
    >>> matrix = [[3, 6, 5][float('nan'), 1, 0]]
    >>> print(matrix_divided(matrix, float('nan'))
    [[nan, nan, nan], [nan, nan, nan]]

Test(missing one argument):
    >>> matrix = [[1, 2][2, 5]]
    >>> print(matrix_divided(matrix))
    Traceback (most recent call last):
    ...
    TypeError: matrix_divided() missing 1 required positional argument: 'div'

Test(missing 2 arguments):
    >>> print(matrix_divided())
    Traceback (most recent call last):
    ...
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
