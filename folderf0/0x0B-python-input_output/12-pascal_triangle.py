#!/usr/bin/python3
"""module for pascal tringle"""


def pascal_triangle(n):
    """this function returns a list of lists of integers
    representing the Pascal's triangle of n"""
    nums = [[1 for a in range(b + 1)] for b in range(n)]
    for i in range(n):
        for j in range(i - 1):
            nums[i][j + 1] = sum(nums[i - 1][j:j + 2])
    return nums
