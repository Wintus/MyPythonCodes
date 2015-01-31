class AtoZ():
    def __init__(self):
        self.atoz = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
##        list(map(chr, range(ord('A'), ord('Z')+1)))
    
    def __iter__(self):
        self.atoz = list(map(chr, range(ord('A'), ord('Z')+1)))
        return self

    def __next__(self):
        if not self.atoz:
            raise StopIteration
        char = self.atoz.pop(0)
        return char

    def __call__(self):
        return self.atoz.pop(0)

    def lower(self):
        self.atoz = [c.lower() for c in self]
        return self

def pyramid():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = 1
    while s:
        print(s[:n])
        s = s[n:]
        n += 1

if __name__ == '__main__':
    print("AtoZ:", list(AtoZ()))
    print("a2z:", list(AtoZ().lower()))
