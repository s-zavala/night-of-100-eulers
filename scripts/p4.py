"""
Find the largest palindrome that is the product of two three-digit numbers.
"""
from palindromes import number_list
from rho import primality_test
from math import prod

pal_list = number_list()

for num in pal_list:
    factors = primality_test(num)
    if factors[-1] < 1000:
        # All palindromes base 10 that are 6 digits long are divisible by 11.
        quotient = num / 11
        # The upper bound is 999*90 b/c 11 * x < 1000.
        if quotient < 89910:
            print(f'Palindrome {num} has factors {factors}.')

# The smallest palindrome that is a product of two 3 digit numbers is 10201.
# The largest number that is the product of two 3 digit numbers is 998001.
# The next palindrome less than this number is 997799, before 998899.