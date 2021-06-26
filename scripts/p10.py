#!/usr/bin/env python
"""
Find the sum of all primes less than two million.
"""
import miller_rabin_test


primes = (p for p in range(3, 2000000, 2) if miller_rabin_test.miller_test(n=p, k=75))
print(sum(primes)+2)


