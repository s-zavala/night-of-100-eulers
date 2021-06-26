#!/usr/bin/env python
"""
Find the greatest product of four integers in the grid.
Numbers must be consecutive top to bottom, left to right, or diagonal.
"""
from math import prod
import numpy as np


def read_numbers():
    fhan = open("/home/sofia-desktop/Code/project-euler/scripts/p11_grid.txt")
    lines = []
    for line in fhan:
        line = line.split('\n')[0]
        line = line.split()
        line = [int(num) for num in line]
        lines.append(line)
    return lines

# How do I read in data from a txt file?
lines = read_numbers()
data = np.array(lines, int)
print(data)