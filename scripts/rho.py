"""
Pollard's rho algorithm
"""
from math import gcd, prod

def polynomial(x, n):
    return (x * x + 1) % n

def rho_algo(n):
    d = 1
    x = 2
    y = 2

    while d == 1:
        x = int(polynomial(x, n))
        y  = int(polynomial(polynomial(y, n), n))
        d = gcd(int(abs(x - y)), n)
    if d == n:
        return 'Done.'
    else:
        return d

def primality_test(n):
    primes = []
    if rho_algo(n) == 'Done.':
        primes.append(n)
    else:
        first = int(rho_algo(n))
        primes.append(first)
        check = n
        while check / first != 1:
            m = int(check / first)
            next = rho_algo(m)
            if next == 'Done.':
                primes.append(int(n / prod(primes)))
                break
            else:
                primes.append(next)
                check = check / next
    return primes

if __name__ == '__main__':
    primality_test(n=12121)

