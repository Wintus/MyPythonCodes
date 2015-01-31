'''Prime Checker'''

def is_prime(n):
    '''check if interger n is a prime'''

    n = abs(int(n)) # n is a pesitive integer
    if n < 2:
        return False
    elif n == 2:
        return True
    # all even ns aren't primes
    elif not n & 1: # bit and
        return False
    else:
        # for all odd ns
        for x in range(3, int(n ** .5) + 1, 2):
            if n % x == 0:
                return False
        else:
            return True

if __name__ == '__main__':
    # test
    ns = (1, 2, 3, 29, 49, 95, 345, 999979, 999981) # FTTTFFFTF
    for n in ns:
        print(n, is_prime(n))
