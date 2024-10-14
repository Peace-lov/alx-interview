#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes
can be opened.
"""


def canUnlockAll(boxes):
    """
    Description:
    A key with the same number as a box opens that box
    Assume all keys will be positive integers
    Though there can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return
    False
    """
    MyKeys = [0]
    for k in MyKeys:
        for BoxKey in boxes[k]:
            if BoxKey not in MyKeys and BoxKey < len(boxes):
                MyKeys.append(BoxKey)
    if len(MyKeys) == len(boxes):
        return True
    return False
