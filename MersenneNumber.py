'''Mersenne Number'''

from PrimeChecker import is_prime

def mersenne(n):
    return 2 ** n - 1

if __name__ == '__main__':
    print("Mersenne Numbers")
    for i in range(1, mersenne(5) + 1):
        m = mersenne(i)
        print("{:2}: {:10}, {}".format(i, m, \
                                       "Prime" if is_prime(m) else "Not"))
