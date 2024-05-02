def canUnlockAll(boxes):
    """A method that determines if all
    boxes can be unlocked"""

    unlocked_boxes = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes
            and key != box_id:
                unlocked_boxes.append(key)
    if len(boxes) == len(unlocked_boxes):
        return True
    return False
