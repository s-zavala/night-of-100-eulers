"""
Find the 10,001th prime number.
"""
import random

def prime_no_theorem(n):
    from math import log
    return n / log(n)
# Estimate the closest number greater than the 10,001th prime.
estimate = prime_no_theorem(n=117000)
print(estimate)

def miller_test(n, k):
    """
    n: a positive integer to test for primality
    k: a positive integer for repetitions of test
    Return True if n is probably prime, else False.
    """
    def fermat():
        count = 0
        while count <= r - 1:
            x = pow(a, (2**r) * d, n)
            if (x == 1) or (x == n - 1):
                # n is probably prime
                return True
            else:
                count += 1
        # If x is neither 1 nor n - 1 then a is a composite witness.
        return False

    flag = None
    # Write n as 2^r*d + 1 by factoring powers of 2 from n - 1.
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d /= 2
    d = int(d)

    # Witness loop, repeat k times.
    for rep in range(k):
        a = random.randrange(2, n-2)
        flag = fermat()
        if flag == True:
            # Continue loop in case a is a liar.
            continue
        else:
            return flag
    return flag

# print(miller_test(n=101, k=5))

primes = [2, 3]
for num in range(5, 117000, 2):
    if len(primes) > 10000: break
    if miller_test(n=num, k=12) == True:
        primes.append(num)
print(primes[-1])
print(len(primes))