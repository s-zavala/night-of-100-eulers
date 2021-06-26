#!/usr/bin/env python
"""
Index for diagonals
"""
from math import prod


def diagonals(x_range, y_range, tr_bl: bool):
    """
    Return diagonals through a 20x20 grid.
    A list of lists of tuples representing indexes.
    """
    def coordinates(x_range, y_range):
        coor = []
        if tr_bl: target = x_range
        else:
            target = y_range
        while target:
            diagonal = list(zip(x_range, y_range))
            coor.append(diagonal)
            target.pop(0)
        return coor
    coor_1 = coordinates(x_range[:], y_range[:])
    if tr_bl:
        x_range.pop(0)
        y_range.pop(-1)
    else:
        x_range.pop(-1)
        y_range.pop(0)
    coor_2 = coordinates(x_range[:], y_range[:])
    return coor_1 + coor_2

top_left_bottom_right = diagonals(x_range=list(range(0,19+1)), y_range=list(range(0, 19+1)), tr_bl=True)
bottom_left_top_right = diagonals(x_range=list(range(0,19+1)), y_range=list(range(19,-1, -1)), tr_bl=False)

# Import 20x20 grid from projecteuler.com
fhan = open("/home/sofia/Code/project-euler/scripts/p11.txt")
euler_grid = []
for line in fhan:
    line = line.splitlines()[0]
    line = line.split()
    line = [int(x) for x in line]
    euler_grid.append(line)
# print(euler_grid)

def euler_values(coor):
    diagonal_values = []
    for row in coor:
        values = []
        for (x,y) in row:
            values.append(euler_grid[x][y])
        diagonal_values.append(values)
    return diagonal_values

tl_br_values = euler_values(coor=top_left_bottom_right)
bl_tr_values = euler_values(coor=bottom_left_top_right)

def find_max_product(diagonal_values):
    highest = 0
    for row in diagonal_values:
        groups = [row[i:i+4] for i in range(len(row))]
        for group in groups:
            p = prod(group)
            if p > highest: highest = p
    return highest

ans = find_max_product(bl_tr_values)
print(ans)