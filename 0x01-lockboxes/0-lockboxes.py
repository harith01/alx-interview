#!/usr/bin/python3
"""Unlock boxes"""


def canUnlockAll(boxes):
"""
    :type boxes: List[List[int]]
    :rtype: bool
"""
    unlocked = set([0])
    while unlocked:
        box = unlocked.pop()
        for key in boxes[box]:
            if key not in unlocked:
                unlocked.add(key)
    return len(unlocked) == len(boxes)
