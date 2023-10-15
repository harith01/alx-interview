def canUnlockAll(boxes):
    """Unlock boxes"""
    counts = 0
    save_keys = dict()

    while counts < len(boxes):
        for key in boxes[counts]:
            if key != counts:
                save_keys[key] = key
        counts += 1

    return (len(save_keys) == len(boxes) or len(save_keys) == len(boxes) -1)
