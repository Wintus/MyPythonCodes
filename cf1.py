class ContinuedFraction():
    """Continued Fraction. number -> [int]"""

    def __init__(self, n):
        self.n = n
        self.n_list = cfrac(self.n)

    def __iter__(self):
        self.head = int(self.n)
        return self.head

class cf(ContinuedFraction):
    """Another shorter name version"""

if __name__ = '__main__':
    cf1 = cf(.0726)
    print(cf1)
