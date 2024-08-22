#!/usr/bin/python3
"""
Creating a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    list of integers 'n'
    Args:
    n (int): base number for calculating triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    for row in range(n):
        n_row = []
        triangle.append(n_row)
        n_row.append(1)
        for j in range(1, row):
            n_row.append(triangle[row - 1][j - 1] + triangle[row - 1][j])
        if row > 0:
            n_row.append(1)
    return triangle
