'''recursion to tail call''' # seems impossible

from functools import wraps

def tail_call(func):
    '''decorate function to tail call form'''
    def _tail_call(*args, **key):
        nonlocal = func
        
    return _tail_call

@tail_call
def frac(n):
    return 1 if n == 0 else n * frac(n - 1)

# =>

def frac_TC(n, acc=1):
    return acc if n == 0 else frac(n - 1, acc * n)
