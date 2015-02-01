from functools import reduce
from operator import mul

def at_least_one_success(ns):
    """alos(iter) -> num
    all n in iter: 0 <= n <= 1"""
    if not any(map(lambda n: 0 <= n <= 1, ns)):
        raise ValueError
    inverse = lambda n: 1 - n
    product = lambda ns: reduce(mul, ns)
    return inverse(product(map(inverse, ns)))
