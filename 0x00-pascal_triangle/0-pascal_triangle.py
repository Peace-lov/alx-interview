#!/usr/bin/python3
"""
Creating a pascals triangle
"""
def pascal_triangle(n):
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
