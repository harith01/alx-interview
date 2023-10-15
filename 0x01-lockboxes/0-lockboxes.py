#!/usr/bin/python3
"""Lockbox"""

def canUnlockAll(boxes):
    counts = 0
    save_keys = dict()

    # Looping through the boxes
    while counts < len(boxes):
        for key in boxes[counts]:
            # Check if a box's key is in the box, if yes, ignore.
            if key != counts:
                save_keys[key] = key
        counts += 1

    return (len(save_keys) == len(boxes) or len(save_keys) == len(boxes) -1)
