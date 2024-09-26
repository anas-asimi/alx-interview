#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate 2D matrix 90 degrees clockwise"""
    # schema:
    # +-----+-----+-----+
    # |  a  |  →  |  b  |
    # +-----+-----+-----+
    # |  ↑  |     |  ↓  |
    # +-----+-----+-----+
    # |  d  |  ←  |  c  |
    # +-----+-----+-----+
    # a, b, c, d = d, a, b, c
    columns = len(matrix[0])
    rows = len(matrix)
    for i in range(0, int(rows/2)):
        for j in range(i, columns - 1 - i):
            a = matrix[i][j]
            b = matrix[j][- 1 - i]
            c = matrix[- 1 - i][- 1 - j]
            d = matrix[- 1 - j][i]
            # swap
            matrix[i][j] = d
            matrix[j][- 1 - i] = a
            matrix[- 1 - i][- 1 - j] = b
            matrix[- 1 - j][i] = c
