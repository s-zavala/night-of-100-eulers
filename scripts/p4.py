"""
Find the largest palindrome that is the product of two three-digit numbers.
"""
from palindromes import number_list
from rho import primality_test

pal_list = number_list()

for num in pal_list:
    factors = primality_test(num)
    if factors[-1] < 1000:
        print(f'Palindrome {num} has factors {factors}.')