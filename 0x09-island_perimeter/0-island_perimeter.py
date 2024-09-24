#!/usr/bin/python3
"""This code is for Island Perimeter"""


def island_perimeter(grid):
    """
    grid is a list of integers:
    0 shows water
    1 shows land
    Each of the cells is square, coupled with a side length of 1
    Cells are connected horizontally/vertically
    grid is rectangular, coupled with its width and height not exceeding 100
    """
    per = 0
    for g in range(len(grid)):
        for h in range(len(grid[g])):
            if grid[g][h] == 1:
                if g == 0 or grid[g - 1][h] == 0:
                    per += 1
                if h == 0 or grid[g][h - 1] == 0:
                    per += 1
                if g == len(grid) - 1 or grid[g + 1][h] == 0:
                    per += 1
                if h == len(grid[g]) - 1 or grid[g][h + 1] == 0:
                    per += 1
    return (per)
