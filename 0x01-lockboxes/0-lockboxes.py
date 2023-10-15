#!/usr/bin/python3
"""Lockbox"""


def canUnlockAll(boxes):
    """A function that determines if all lockboxes can be opened"""
    keys = []

    for i in range(len(boxes)):
        for key in boxes[i]:
            if key != i and key < len(boxes):
                keys.append(key)
    keys = set(keys)
    return (len(keys) == len(boxes))
