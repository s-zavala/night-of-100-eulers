"""
05/20/2021
"""
target = 600851475143
square_root = int(target ** 0.5)

def is_prime(target):
    """
    
    """
    square_root = int(target ** 0.5)
    # End search at squareroot of the target.
    def scan():
        # Test 2 divides target.
        if target % 2 != 0: yield True
        else:
            yield False
        for _ in range(3, square_root, 2):
            yield target % _ != 0
    return all(scan())

# print(is_prime())

def sieve_of_eratosthenes(target):
    """
    Make me a list of primes below the square root of my target that I can search for prime factors.
    """
    square_root = int(target ** 0.5)
    primes = []
    def prime_factor(num):
        """ Mark a num as a factor of a prime. Is num % prime == 0 for any prime?
        Given a number, return True if not divisible by any number in primes list.
        False, otherwise.
        """
        flag = True
        for prime in primes:
            if num % prime == 0:
                # if there is a prime that is a factor of num then num is a composite.
                # print(f'{num} has a prime factor {prime}')
                flag = False
            else:
                continue
        return flag
    for num in range(2, square_root+1):
        if not primes:
            primes.append(num)
            continue
        if prime_factor(num):
            primes.append(num)
    return primes

def prime_no_theorem(wall):
    from math import log
    return wall / log(wall)


s = sieve_of_eratosthenes(target=2000000)
print(sum(s))
# print(prime_no_theorem(square_root))

# my_range = range(775046, 775146)
# for num in my_range.__reversed__():
#     print(num, is_prime(num))

# largest_prime = 775121
# largest_prime_bin = bin(largest_prime)

# print(target / largest_prime)