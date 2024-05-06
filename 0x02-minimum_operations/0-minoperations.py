#!/usr/bin/python3
"""Minimum Copy-Paste Operations"""


def minOperations(n):
    """Calculates the fewest number of copy
    -paste operations"""

    current_length = 1
    operations = 0
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1
        current_length += clipboard
        operations += 1

    return operations
