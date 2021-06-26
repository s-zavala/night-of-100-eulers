#!/usr/bin/env python
"""
A recursive attempt at problem 11.
"""
fhan = open("scripts/p11.txt")
grid = []
for line in fhan:
    line = line.splitlines()[0]
    line = line.split()
    line = [int(num) for num in line]
    grid.append(line)

def test_adjacent(test_x, test_y):
    """
    TL ML TR
    ML -- MR
    BL ML BR
    """
    # Make an empty list to store four coordinate tuples.
    prod = 0
    # Define the size of a group of adjacent numbers.
    group_len = 4 - 1
    def recur_test(x, y, shift):
        shifts = {'tl': (x+1, y+1),
                'tm': (x+1, y),
                'tr': (x+1, y-1),
                'ml': (x, y+1),
                'mr': (x, y-1),
                'bl': (x-1, y+1),
                'bm': (x-1, y),
                'br': (x-1, y-1)}
        if (x, y) == (test_x, test_y):
            return x, y
        try:
            if (grid[x][y] // 10 == 9) or (grid[x][y] // 10 == 8) or (grid[x][y] //10 == 7):
                print(grid[x][y])
                return grid[x][y] * recur_test(shifts[shift][0], shifts[shift][1], shift)
        except IndexError:
            return 0
        else:
            return 0
    shift_4 = {'tl': (test_x - group_len, test_y - group_len),
                'tm': (test_x - group_len, test_y),
                'tr': (test_x - group_len, test_y + group_len),
                'ml': (test_x, test_y - group_len),
                'mr': (test_x, test_y + group_len),
                'bl': (test_x + group_len, test_y - group_len),
                'bm': (test_x + group_len, test_y),
                'br': (test_x + group_len, test_y + group_len)}
    for direction in shift_4.keys():
        x = recur_test(x=shift_4[direction][0], y=shift_4[direction][1], shift=direction)
        if x > prod:
            prod = x
    return prod

for row in grid:
    print(row)
    for num in row:
        if num // 10 == 9:
            print(num)
            prod = test_adjacent(test_x=grid.index(row), test_y=row.index(num))
            if prod: print(prod)