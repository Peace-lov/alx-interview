#!/usr/bin/python3
"""Module for 0-minoperations"""


def minOperations(n):
    """
    Calculating the fewest number of operations needed to result in exactly n H characters
    """
    if (n < 2):
        return 0
    op = 0
    div = 2
    while div <= n:
        if n % div == 0:
            op += div
            n = n / div
            div -= 1
        div += 1
    return op
