'''Pyramid iterator'''

class Pyramid():
    '''iterable -> list of increasing list

    ex. [[A],[B, C], [D, E, F], ... ]'''

    def __init__(self, iterable):
        self.itr = iterable
        self.pyramid = make_pyramid(self.itr)

    def __iter__(self):
        self.p_list = []
        self.count = 1
        return self

    def __next__(self):
        pass
        
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 1
while s:
    print(s[:n])
    s = s[n:]
    n += 1
