"""
Pollard's rho algorithm
"""
from math import gcd, prod

def polynomial(x, n):
    return (x * x + 1) % n

def rho_algo(n, x):
    # Start the divisor at one.
    d = 1
    y = x
    # x and y are used to generate pseudo random numbers with the polynomial function.
    # x = 2
    # y = 2

    # Keep searching for divisors other than one.
    while d == 1:
        # x is assigned the output of the polynomial mod n.
        x = int(polynomial(x, n))
        # y is assigned the output of the poly of the poly of y mod n.
        y  = int(polynomial(polynomial(y, n), n))
        # d is the greatest common divisor of the absolute value of the difference of x and y with n.
        d = gcd(int(abs(x - y)), n)
    # If the divisor is not one and also it is n then return flag 'Done.'.
    if d == n:
        return 'Done.'
    # Else the divisor is not one and not n. Return the divisor.
    elif d == 0: pass
    else:
        return d

def primality_test(n):
    """
    Returns prime factorization.
    """
    primes = []
    for x in range(2, 20):
        if rho_algo(n, x) == 'Done.':
            primes.append(n)
        else:
            first = int(rho_algo(n, x))
            primes.append(first)
            check = n
            while check / first != 1:
                m = int(check / first)
                next = rho_algo(m, x)
                if next == 'Done.':
                    q = int(n / prod(primes))
                    if q != 0:
                        primes.append(q)
                    break
                else:
                    primes.append(next)
                    check = check / next
    return True if len(set(primes)) == 1 else False
    # return set(primes)

if __name__ == '__main__':
    print(primality_test(n=25))

