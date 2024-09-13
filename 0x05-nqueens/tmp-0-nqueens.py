#!/usr/bin/python3
"""
0-nqueens.py
"""
import sys


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

for i in range(1, N-1):
    first_queen = [0, i]
    solution = [first_queen]
    for j in range(1, N):
        used_rows = [queen[1] for queen in solution]
        last_row = used_rows[-1]
        current_queen = [j, N-1]
        for x in range(0, N):
            if x not in used_rows and x is not last_row+1 and x is not last_row-1:
                current_queen[1] = x
                break
        # if last_queen_row+2 < N:
        #     queen = [j, last_queen_row+2]
        # else:
        #     queen = [j, last_queen_row-N+2]
        solution.append(current_queen)
    print(solution)
    print_board(N, solution)
    print()
