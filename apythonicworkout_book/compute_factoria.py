from math import factorial


def to_infinity(n):
    n = factorial(n)
    return n * n/1


print(to_infinity(5))
