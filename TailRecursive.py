'''tail recursion decorator'''

from functools import wraps

class Continue(object):pass

def tail_recursive(func):
    print('Initialize')
    first_call = True
    CONTINUE = Continue()
    args_kwd = None
    
    @wraps(func)
    def _tail_recursive(*args, **kwd):
        print('inner_func')
        print('given_args:\t', args, kwd)
        nonlocal func, first_call, CONTINUE, args_kwd # closure
        if first_call == True:
            print('first_call')
            first_call = False
            try:
                count = 0
                while True:
                    count += 1
                    print('loop:', count)
                    print('call_func')
                    result = func(*args, **kwd)
                    # label: A
                    if result is CONTINUE:  # update arguments
                        print('continued')
                        args, kwd = args_kwd
                        print('updated_args:\t', args, kwd)
                    else: # last call
                        print('end')
                        return result
            finally:
                print('finally')
                first_call = True # prepare for the next call
        else: # return the arguments of the tail call
            print('non-first_call')
            args_kwd = args, kwd
            print('tail-call_args:\t', args_kwd)
            print('continue')
            return CONTINUE # goto A
    return _tail_recursive


if __name__ == '__main__':
    @tail_recursive
    def sum_to(n, acc=0):
        return acc if n == 0 else sum_to(n-1, acc+n)

    n = 10#0000
    print("The sum from 1 to {}:".format(n), sum_to(n))
    print()
    
    def fib(n):
        @tail_recursive
        def _fib(a, b, n):
            return _fib(b, a+b, n-1) if n > 0 else a
        return _fib(0, 1, n)

    n = 10#00
    print("fibbnacci number of the {}th:".format(n), fib(n))
    print()

    @tail_recursive
    def fact(n, acc=1):
        return acc if n == 0 else fact(n-1, n*acc)
    
    n = 10#0
    print("factorial of {}:".format(n), fact(n))
