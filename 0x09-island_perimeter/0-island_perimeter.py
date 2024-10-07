#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def get_touched_sides(y: int, x: int, grid) -> int:
    """get_touched_sides"""
    touched_sides = 0
    if y >= 1 and grid[y-1][x] == 1:
        touched_sides += 1
    if y < (len(grid) - 1) and grid[y+1][x] == 1:
        touched_sides += 1
    if x >= 1 and grid[y][x-1] == 1:
        touched_sides += 1
    if x < (len(grid[y]) - 1) and grid[y][x+1] == 1:
        touched_sides += 1
    return touched_sides


def island_perimeter(grid) -> int:
    """island_perimeter"""
    perimeter = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                touched_sides = get_touched_sides(y, x, grid)
                if touched_sides < 4 and touched_sides > 0:
                    perimeter += get_touched_sides(y, x, grid)
    return perimeter
