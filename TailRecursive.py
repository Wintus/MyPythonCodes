'''tail recursion decorator'''

from functools import wraps

class Continue(object):pass

def tail_recursive(func):
    first_call = True
    CONTINUE = Continue()
    args_kwd = None
    
    @wraps(func)
    def _tail_recursive(*args, **kwd):
        nonlocal func, first_call, CONTINUE, args_kwd # closure
        if first_call:
            first_call = False
            try:
                while True:
                    result = func(*args, **kwd)
                    if result is CONTINUE:  # update arguments
                        args, kwd = args_kwd
                    else: # last call
                        return result
            finally:
                first_call = True # prepare for the next call
        else: # return the arguments of the tail call
            args_kwd = args, kwd
            return CONTINUE
    return _tail_recursive


if __name__ == '__main__':
    @tail_recursive
    def sum_to(n, acc=0):
        return acc if n == 0 else sum_to(n-1, acc+n)

    n = 100000
    print("The sum from 1 to {}:".format(n), sum_to(n))
    print()
    
    def fib(n):
        @tail_recursive
        def _fib(a, b, n):
            return _fib(b, a+b, n-1) if n > 0 else a
        return _fib(0, 1, n)

    print("fibbnacci number of 1000th:", fib(1000))
    print()

    @tail_recursive
    def fact(n, acc=1):
        return acc if n == 0 else fact(n-1, n*acc)

    print("factorial of 100:", fact(100))
    print()
