"""
Three is a lucky number!
05/21/2021
"""

def fermat_primality(a, p):
    print(f'A: {a}')
    print(f'P: {p}')
    fermat = (a ** (p - 1)) % p
    print(f'Fermat: {fermat}')

# for a in range(1, 20):
#     fermat_primality(a, p=101)

from random import randrange
from itertools import count
from math import gcd
import sys

number = 600851475143
x = 35
# number = 10403
# x = 2

"""
Pollard's rho algorithm
https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
"""
for cycle in count(1):
    y = x
    for i in range(2 ** cycle):
        x = (x * x + 1) % number
        factor = gcd(x - y, number)
        if factor > 1:
            print("factor is", factor)
            sys.exit()
