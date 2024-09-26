#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix


def print_2d_matrix(data):
    """Printing a 2D array as a table with borders"""
    if not data:
        return
    num_cols = len(data[0])
    col_width = 5
    horizontal_line = "+" + "+".join(["-" * col_width] * num_cols) + "+"

    print(horizontal_line)
    for row in data:
        print("|" + "|".join([f" {str(item):^3} " for item in row]) + "|")
        print(horizontal_line)


def create_array_2d(dimension):
    """Creating a 2D array with incrementing numbers"""
    return [[row * dimension + col + 1 for col in range(dimension)] for row in range(dimension)]


if __name__ == "__main__":
    matrix = create_array_2d(9)
    print('fist:')
    print_2d_matrix(matrix)

    rotate_2d_matrix(matrix)
    print('last:')
    print_2d_matrix(matrix)
