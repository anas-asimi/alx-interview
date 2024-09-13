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


def print_board(size, pieces):
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
    current_col = len(queens)
    for row in range(0, N):
        current_position = [current_col, row]
        is_attacked_by = [is_attacking(current_position, queen)
                          for queen in queens]
        if not any(is_attacked_by):
            new_queens = queens + [current_position]
            if len(new_queens) == N:
                return new_queens
            else:
                solution = get_solution(N, new_queens)
                if solution is not None:
                    return solution


for i in range(1, N-1):
    """
    solutions finder
    """
    first_queen = [0, i]
    solution = get_solution(N, [first_queen])
    print(solution)
    # print_board(N, solution)
    print()

# for i in range(1, N-1):
#     """
#     solutions finder
#     """
#     first_queen = [0, i]
#     solution = [first_queen]
#     for j in range(1, N):
#         """
#         solution positions finder
#         """
#         for x in range(0, N):
#             """
#             checking possible position
#             """
#             current_position = [j, x]
#             is_attacked_by = [is_attacking(
#                 current_position, queen) for queen in solution]
#             if not any(is_attacked_by):
#                 solution.append(current_position)
#                 continue
#     print(solution)
#     print()
