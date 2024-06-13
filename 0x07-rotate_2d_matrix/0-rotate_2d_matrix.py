#!/usr/bin/python3
"""
Rotate a nxn matrix 90 degrees
clockwise
"""


def rotate_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            c = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = c
    for i in matrix:
        i.reverse()
