'''unzip'''

def unzip(*zipped):
    return zip(*zipped)

if __name__ == '__main__':
    a = range(5)
    b = "ABCDE"
    zipped = tuple(zip(a, b))
    w = 10
    print("A:".ljust(w), *a)
    print("B:".ljust(w), *b)
    print("Zipped:".ljust(w), *zipped)
    print("Unzipped:".ljust(w), *unzip(*zipped))
