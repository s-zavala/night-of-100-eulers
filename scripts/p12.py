#!/usr/bin/env python
"""
Find the smallest triangular number that has more than 500 divisors.
"""
"""
Pseudo-code algorithm
Input: n, a counting number
1. Calculate the nth triangular number, x.
2. Find all divisors of n.
3. Find all divisors of n+1.
4. Find all combinations products of n-divisors * n+1-divisors, without replacement.
5. Test each product to see if it is a divisor of x.
    5a. If the product == x, stop.
    5b. Yes, then store the product and x/product in a list.
6. Remove all duplicates from list.
7. Add len(list) + 1 + 1 (for x, itself, and 1)
8. Return if sum > 500.
Output: True or False
"""