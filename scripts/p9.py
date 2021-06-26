#!/usr/bin/env python
"""
Find the pythagorean triple for a + b + c = 1000.
"""
from math import sqrt, prod
from itertools import combinations

flag = False

def poly(a, b):
    return (1000000 - (2000 * a) - (2000 * b) + (2 * a * b))

for a, b in combinations(range(1, 1000), 2):
    if poly(a, b) == 0:
        ans = prod((a, b, (sqrt(a**2+b**2))))
        print(ans)