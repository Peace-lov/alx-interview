#!/usr/bin/python3
"""
Creating a pascals triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for row in range(n):
        triangle_row = [1 if j == 0 or j == row else triangle[row - 1][j - 1] + triangle[row - 1][j] for j in range(row + 1)]
        triangle.append(triangle_row)
    return triangle
