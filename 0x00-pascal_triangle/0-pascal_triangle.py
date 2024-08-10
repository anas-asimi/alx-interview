#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    triangle = []
    for row in range(1, n + 1):
        rowElements = []
        if row == 1:
            rowElements.append(1)
        else:
            previousRow = triangle[-1]
            for i in range(row):
                if i == 0 or i == (row - 1):
                    x = 1
                else:
                    x = previousRow[i-1] + previousRow[i]
                rowElements.append(x)
        triangle.append(rowElements)
    return triangle
