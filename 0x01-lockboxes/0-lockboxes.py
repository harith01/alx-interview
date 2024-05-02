#!/usr/bin/python3
"""
Determine if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """A method that determines if all
    boxes can be unlocked"""

    un_boxes = [0]
    for b_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in un_boxes and key != b_id:
                un_boxes.append(key)
    if len(boxes) == len(un_boxes):
        return True
    return False
