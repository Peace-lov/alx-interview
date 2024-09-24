#!/usr/bin/python3
"""The program that will perform a prime game"""


def isWinner(x, nums):
    """The function that will perform the prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    ft = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not ft[i]:
            continue
        for j in range(i * i, n + 1, i):
            ft[j] = False
    ft[0] = ft[1] = False
    c = 0
    for i in range(len(ft)):
        if ft[i]:
            c += 1
        ft[i] = c
    ply1 = 0
    for n in nums:
        ply1 += ft[n] % 2 == 1
    if ply1 * 2 == len(nums):
        return None
    if ply1 * 2 > len(nums):
        return 'Maria'
    return 'Ben'
