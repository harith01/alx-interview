#!/usr/bin/python3
"""Lockbox"""


def canUnlockAll(boxes):
    """A function that determines if all lockboxes can be opened"""

    if len(boxes[0]) == 0:
        return False

    checked = []
    to_be_checked = boxes[0]

    for key in to_be_checked:
        if key not in checked:
            to_be_checked.extend(boxes[key])
            checked.append(key)

    return (len(checked) == len(boxes) or len(checked) == len(boxes) - 1)
