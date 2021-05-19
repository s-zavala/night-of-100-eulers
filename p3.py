"""
05/19/2021
Problem 3
Find the largest prime factor of 600851475143
"""
TARGET = 600851475143

def is_prime(n):
    def scan():
        for _ in range(2, n):
            yield n % _ != 0
    return all(scan())

def largest_prime_factor(n):
    prime_list = (_ for _ in range(2, n//2) if is_prime(_))
    # def prime_list():
    #     for _ in range(2, n+1):
    #         if is_prime(_):
    #             yield _
    prime_factors = (_ for _ in prime_list if n % _ == 0)
    # def factor(x):
    #     if n % x == 0:
    #         yield x
    print(max(prime_factors))

largest_prime_factor(n=TARGET)
