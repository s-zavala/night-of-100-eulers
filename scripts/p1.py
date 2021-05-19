#!/usr/bin/env python
"""
Find the sum of all multiples of 3 or 5 below 1000.
"""
def mult_3_or_5(n):
    # Base Case.
    if n == 3:
        # Terminate recursion.
        return 3
    # Test.
    if n % 3 == 0 or n % 5 == 0:
        # Function calls itself.
        return n + mult_3_or_5(n - 1)
    else:
        return mult_3_or_5(n-1)

def gen_mult():
    for num in range(1000):
        if not num % 3 or not num % 5:
            yield num
gen_ans = sum(gen_mult())
print('Generator answer:', gen_ans)

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def sum_in_range(n):
    return sum(num for num in range(n))

if __name__ == '__main__':
    # print(factorial(n=10))
    print(mult_3_or_5(999))
    # print(sum_in_range(999))
