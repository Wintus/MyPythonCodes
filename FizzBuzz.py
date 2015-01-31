'''FizzBuzz'''

def fizzbuzz(ns):
    '''number sequence -> tuple'''
##    def gcd(a, b):
##        while b:
##            a, b = b, a % b
##        return a
##    _fizzbuzz = lambda n: (lambda n: "FizzBuzz" if n == 15 \
##                           else ("Fizz" if n == 3 \
##                                 else ("Buzz" if n == 5 else n)))(gcd(n, 15))
##    return tuple(map(_fizzbuzz, ns))

    return tuple(map(lambda n: "FizzBuzz" if n % 15 == 0 \
                     else ("Fizz" if n % 3 == 0 \
                           else ("Buzz" if n % 5 == 0 else n)
                           )
                     , ns))

if __name__ == '__main__':
    for i in fizzbuzz(range(100)):
        print(i, end=' ')
