#!/usr/bin/env python
"""
Find the greatest product of four adjacent numbers in the grid in any formation.
"""
# Hash tables might be a good approach because a grid is like a table.
# But I don't know how to use them.
# Dictionaries are a python data type implementation of hash tables.
# This tool is not best for this problem because it represents key, value pairs and not multi-dimensional arrays.
# Try to use numpy arrays and strides next time.
from math import prod


fhan = open("/home/sofia-desktop/Code/project-euler/scripts/p11_grid.txt")
lines = []
for line in fhan:
    line = line.split('\n')[0]
    line = line.split()
    line = [int(num) for num in line]
    lines.append(line)

horiz = []
# loop over each row, a list containing 20 integers.
for line in lines:
    # slice new lists, four elements long. Find the product of the four.
    # return a list of these products.
    group_products = [prod(line[i: i+4]) for i, elem in enumerate(line)]
    # Append the highest product to horiz.
    horiz.append(max(group_products))
# Find the highest product.
print(max(horiz))

vert = []
def vert_shift():
    reps = len(lines[0])
    columns = []
    for num in range(reps):
        column = []
        for line in lines:
            column.append(line[num])
        columns.append(column)
    return columns
vert_lines = vert_shift()
for line in vert_lines:
    group_products = [prod(line[i: i+4]) for i, elem in enumerate(line)]
    vert.append(max(group_products))
print(max(vert))

top_left_bottom_right = []
def tl_br_shift():
    # Make a list of diagonal sequences of elements.
    diagonals = []
    # reps is horizontal dimension of grid.
    reps = len(lines[0])
    # a is elem from top left to bottom right.
    a = []
    for num in range(reps):
        a.append(lines[num][num])
    diagonals.append(a)
    # b is diagonal starting at first row second elem.
    row = list(range(0, 19))
    column = list(range(1, 20))
    coor = list(zip(row[:],column[:]))
    b = []
    for x,y in coor:
        b.append(lines[x][y])
    # c is diagonal starting first row at third elem.
    row.pop(-1)
    column.pop()
    print(row, column)
    coor = list(zip(row[:],column[:]))
    c = []
    for x,y in coor:
        c.append(lines[x][y])
    print(c)
    return diagonals
tl_br_shift()

# vertical_lines = []
# for i in range(len(lines[0])):
#     vert_line = []
#     for line in lines:
#         vert_line.append(line[i])
#     vertical_lines.append(vert_line)
# vertical_max = max((greatest_product(line) for line in vertical_lines))
# print(vertical_max)

# # l_to_r_lines = []
# # l_to_r_line = [lines[x][x] for x in range(len(lines[0]))]
# # l_to_r_lines.append(l_to_r_line)
# # l_to_r_line = []
# # for x in range(len(lines[0])):
# #     try:
# #         l_to_r_line.append(lines[x][x+1])
# #     except IndexError: pass
# # l_to_r_lines.append(l_to_r_line)
# # l_to_r_line = []
# # for x in range(len(lines[0])):
# #     try:
# #         l_to_r_line.append(lines[x+1][x])
# #     except IndexError: pass
# # l_to_r_lines.append(l_to_r_line)

# # l_to_r_max = max((greatest_product(line) for line in l_to_r_lines))
# # print(l_to_r_max)


# r_to_l_diagonal = []
# r_to_l_lines = []
# r_to_l_line = []
# for x in range(len(lines[0])):
#     r_to_l_line.append(lines[x][len(lines[0]) - 1 - x])
# r_to_l_lines.append(r_to_l_line)

# count = 18
# while count > 0:
#     for row in range(count + 1):
#         print(row, count - x)
#     count -= 1

# # for y in range(len(lines[0])-1, 0, -1):
# #     r_to_l_line = []
# #     for x in range(len(lines[0])-1):
# #         try:
# #             r_to_l_line.append(lines[x][y-1-x])
# #         except IndexError: pass
# #     r_to_l_lines.append(r_to_l_line)

# # l = []
# # for row, line in enumerate(lines):
# #     d = {}
# #     for column, elem in enumerate(line):
# #         d[(row, column)] = elem
# #     l.append(d)
# # print(l)
