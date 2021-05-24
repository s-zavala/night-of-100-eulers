"""
Find the difference of the square of a sum of numbers 1 -> n and the sum of a the squares of numbers 1 -> n.
"""

def diff_sum_square(n, start=1):
    square_sum = (n * (start + n) / 2) ** 2
    sum_square = n * (n + 1) * (2 * n + 1) / 6
    return square_sum - sum_square

if __name__ == "__main__":
    print(diff_sum_square(n=100))