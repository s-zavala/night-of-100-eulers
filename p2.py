"""
Sum of even Fibonacci numbers below 4 million.
Example:
Fibonacci sequence first ten terms are 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
Sum of the evens is 44.
Answer: 4613732
"""


def even_fiby(max):
    # Exclude zero and start sequence at i = 1.
    i = 1
    # Second elem in sequence is j = 1 + 0
    j = 1
    # Repeat bracket for j less than the given maximum.
    level = 1
    while j < max:
        # Increase j by i and reassign i to j.
        print('Level', level)
        i, j = j, i + j
        level += 1
        # Only yield evens.
        if not j % 2:
            yield j

# ans = sum(even_fiby(4000000))
# print(ans)

def recur_even_fiby(n):
    # global num_fib_calls
    # num_fib_calls += 1
    # Base cases.
    if n == 0 or n == 1:
        return 1
    else:
        return recur_even_fiby(n - 1) + recur_even_fiby(n - 2)


# x = recur_even_fiby(n=32)

def fib_count(n):
    evens = 0
    for i in range(n+1):
        # global num_fib_calls
        # num_fib_calls = 0
        # print('Fib of', i, '=', recur_even_fiby(i))
        if not recur_even_fiby(i) % 2:
            evens += recur_even_fiby(i)
        # print('Fib called', num_fib_calls, ' times.')
    print(evens)

def evens(n):
    for i in range(n+1):
        x = recur_even_fiby(i)
        if not x % 2:
            yield x

print(sum(evens(n=32)))

# fib_count(n=32)
