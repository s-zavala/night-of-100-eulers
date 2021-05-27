"""
Find thirteen adjacent digits in the provided 1000-digit number that have the greatest product.
What is the product?
"""
from math import prod


def number():
    """
    Import 1000 digit number from text file and return as one string.
    """
    fhan = open("/home/sofia-desktop/Code/project-euler/scripts/p8-number.txt")
    number = ''
    for line in fhan:
        line = line.splitlines()
        number += line[0]
    return number

num = [int(n) for n in number()]
d = 13

try:
    groups = (num[i:i+d] for i, elem in enumerate(num))
except IndexError:
    pass
max_prod = max([prod(group) for group in groups])
# max_group = None
# max_prod = 0
# while True:
#     try:
#         group = next(groups_of_13)
#         p = prod(group)
#         if p > max_prod:
#             max_prod = p
#             max_group = group
#     except StopIteration:
#         break

# print(max_group)
print(max_prod)