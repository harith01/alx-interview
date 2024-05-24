#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given dataset represents
    a valid UTF-8 encoding"""

    n = 0
    for c in data:
        if n > 0:
            if c >> 6 != 0b10:
                return False
            n -= 1
        else:
            if c >> 7 == 0:
                n = 0
            elif c >> 5 == 0b110:
                n = 1
            elif c >> 4 == 0b1110:
                n = 2
            elif c >> 3 == 0b1110:
                n = 3
            else:
                return False
    return n == 0
