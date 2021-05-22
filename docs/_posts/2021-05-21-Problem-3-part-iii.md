---
title: "Problem 3 part iii"
date:   2021-05-21 00:00:00 -0400
layout: post
---
#### Three is a lucky number!
How lucky is lucky when you get an answer, but do not understand it? Not very.

The Khan academy series on primality testing concluded with Fermat's Little Theorem. For any positive integer, a, and some prime, p, then the number a^p - a is a multiple of p. Another way to look at this is with modular arithmetic a^p is congruent to a mod p. If a is not divisible by p, then we can rewrite the last statement as a^p-1 is congruent to 1 mod p. This is the basis for Fermat's primality test. Wikipedia it and you will find a nice outline of an algorithm, but watch out for pseudoprimes.

Given input: n = number to test for primality
    k = number of repetitions of test
Return output: Composite if n is composite, which we can prove with 100% certainty when we observe a composite witness. Or probably prime if the we observe the property in the little theorem b/c this applies to all primes and very few composites.
Repeat k times:
1. Pick a random #, a, for 2 < a < sqrt(n)
2. If a^n-1 is not congruent to 1 mod n return Composite.
Return probably prime.

That is a nice(O(klog^2n)), mostly correct prime test. How would this help me find the greatest common prime factor of a ~40 bit number? If I wanted to make an list of primes and check them one by one, but that is too expensive especially if I wanted to test a ~100 or ~500 bit number. At this point I consulted [Stack Overflow](https://stackoverflow.com/questions/1877255/problems-with-prime-numbers) for other algorithms and read up on Pollard's rho algorithm. There is an example of this in python right on the wikipedia page, but I did not get it to work right away. I had to input random numbers for x before I got a solution. I am not 100% confident with the details, but here it goes (in pseudocode).

Input: n = number you want to find prime factors for
    g(x) = a polynomial, you decide, modulo n
    I picked x^2 + 1 mod n so I could compare my algorithm with examples on wikipedia
    x = a starting value, x >= 2, but my tests only worked when I started at x = 35
Output: A prime factor, or failure if it just spits out n.
1. Assign initial values.
```python
    x = your starting value
    y = x
    d = 1
```
2. Make a loop that is entered while d is 1.
```python
    x = g(x) # Apply the polynomial function.
    y = g(g(y)) # I think this name y is actually supposed to remain fixed.
    d = gcd(|x-y|, n) # Import gcd() from math module.
```
3. When loop is exited test if it just spit out n, if not this should return a prime factor d.

I need to rework my answer because right now it is not reproducable. Prime factorization is difficult, but RSA encyrption is a good reason to push through these problems and learn more.
