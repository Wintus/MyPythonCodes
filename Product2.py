'''make kuku'''

from functools import reduce
from itertools import product

def product2(iterables, repeats=1):
    '''return a map iterator'''
    mal = lambda a, b: a * b
    return map(lambda i: reduce(mal, i), product(iterables, repeat=repeats))

if __name__ == '__main__':
    row = range(1, 10)
    col = range(1, 10)
    n   = 9
##    ku2 = list(product2((row, col)))
    ku2 = list(product2(range(1, n + 1), repeats=2))
    bar = '\n' + ('-' * (2 + 2) + '|') * (n + 1)

    # display
    print("Kuku")
    print(" x ", end=" |")
    for i in range(1, n + 1):
        print(" _{}".format(i), end=" |")
    print(bar)
    for r in range(n):
        print(" _{}".format(r + 1), end=" |")
        for c in range(n):
            print(" {:2}".format(ku2.pop(0)), end=" |")
        print(bar)
