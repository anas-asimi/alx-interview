#!/usr/bin/python3
"""
0-nqueens.py
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)

solutions = []


def print_board(size, pieces):
    """
    print_board
    Args:
        size (_type_):
        pieces (_type_):
    """
    # Create an empty board
    board = [['.' for _ in range(size)] for _ in range(size)]
    # Place pieces on the board
    for piece in pieces:
        x, y = piece
        board[y][x] = 'o'  # You can change 'Q' to any piece symbol
    # Print the board
    for row in board:
        print(' '.join(row))


def is_attacking(pos0, pos1):
    """
    Checks if the positions of two queens are in an attacking mode.
    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.
    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def get_solution(N: int, queens: list):
    """
    get_solution
    Args:
        N (int):
        queens (list):
    Returns:
        _type_:
    """
    # print(f'queens: {queens}')
    current_col = len(queens)
    if current_col == N:
        solutions.append(queens)
        # print(f'solution: {queens}')
    else:
        for row in range(0, N):
            current_position = [current_col, row]
            new_queens = queens + [current_position]
            is_attacked = False
            for queen in queens:
                if is_attacking(current_position, queen):
                    is_attacked = True
                    break
            if not is_attacked:
                get_solution(N, new_queens)


for i in range(0, N):
    """
    solutions finder
    """
    first_queen = [0, i]
    get_solution(N, [first_queen])

for solution in solutions:
    print(solution)
    # print_board(N, solution)
