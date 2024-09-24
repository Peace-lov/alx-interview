#!/usr/bin/python3
"""This code is for making change"""


def makeChange(coins, total):
    """The function that makes change for a given amount"""
    if total < 1:
        return 0
    chge = 0
    coins.sort(reverse=True)
    for c in coins:
        tmp_chge = int(total / c)
        total -= (tmp_chge * c)
        chge += tmp_chge
        if total == 0:
            return chge
    if total != 0:
        return -1
