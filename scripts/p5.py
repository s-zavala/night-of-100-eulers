"""
Find the smallest number evenly divisible (without any remainder) by all numbers from 1 to 20.
"""
# Any number divisible by 20 is divisible by 2 and 10. 2, 2, 5
# Must be divisible by primes 19, 17, 13, 11, 7, 5, 3, 2.
# 18 factors to 2, 3, 3
# 16 factors to 2, 2, 2, 2
# 15 factors to 3, 5
# 14 factors to 2, 7
# 12 factors to 2, 2, 3
# 10 factors to 2, 5
# 9 factors to 3, 3
# 8 factors to 2, 2, 2
# 6 factors to 2, 3
# 4 factors to 2, 2

# Smallest list with all factors:
# 2, 2, 3, 2, 3, 5, 7, 2, 11, 13, 17, 19
# Product is 232792560

# How do I write my procedure as a program?
# Iterate over 2 to 20.
# Factor each number.
# Make an empty list.
# Iterate over factors.
# If not in list add factor.
# Return product of list.
from math import prod


def smallest_num_divisible():
    '''Find smallest number divisible by all numbers 1 to 20.'''
    def factor(n):
        ''' Return factors of n, for n < 20.'''
        # Primes below 20.
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        factors = []
        # Divide n by each prime until n is a rational number less than 1.
        while n > 1:
            # Check for primes or if n is reduced to a prime.
            if n in primes:
                factors.append(int(n))
                return factors
            for prime in primes:
                if n % prime == 0:
                    factors.append(prime)
                    # Divide until n is smallest prime factor.
                    n /= prime
                    continue
        return factors

    common_factors = []
    for num in range(2, 20):
        factors = factor(n=num)
        if factors not in common_factors:
            # Test whether all factors of num are in common_factors.
            cp = common_factors[:]
            for f in factors:
                if f in cp:
                    cp.remove(f)
                    continue
                else:
                    common_factors.append(f)
    return common_factors

ans = smallest_num_divisible()
print(prod(ans))
