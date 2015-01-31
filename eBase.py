"""e base numeral system"""

import math
e = math.e
base = e
log = math.log
accuracy = 17

class eBase():
    """base: e = 2.718281828459045"""
    def __init__(self, n):
        if isinstance(n, (int, float)):
            self.n = n
        elif isinstance(n, str):
            self.n = to_decimal(n)
        self.digits, self.negative = to_digits(n)

    def __repr__(self):
        n = ('-' if self.negative else '')
        n += ''.join(str(d) for d, p in self.digits if p >= 0)
        frac = [(d, p) for d, p in self.digits if p < 0]
        if to_10(frac):
            n += '.'
            n += ''.join(str(d) for d, p in self.digits if p < 0)
        return n
    
    def __str__(self):
        length = 7 + (1 if self.negative else 0)
        return self.__repr__()[:length]

def to_digits(n, accuracy=12):
    """Return (digits, negative(Bool))"""
    digits = []
    negative = False
    
    if not n:
        digits = (((0, 0),), negative)
        return digits
    elif n < 0:
        negative = True
        n = abs(n)
        
    power = int(log(n)) + 1
    for i in reversed(range(power)):
        d, n = divmod(n, base**i)
        digits.append((int(d), i))

    acc = accuracy - power
    for i in range(acc):
        d, n = divmod(n*e, e)
        digits.append((int(d), -1-i))
        
    return (digits, negative)

def to_10(digits, nagetive=False):
    """return decimal"""
    return sum([digit * (base**place) for digit, place in digits]) * \
           (-1 if nagetive else 1)

def to_decimal(string):
    """interpret a string as a e-base numeral

    return decimal"""
    l = string.split('-')
    if l[-1]: #positive
        negative = False
    elif not l.pop(0): #negative
        negative = True
    i, f = l.pop().split('.')
    n = 0.0
    n += sum([int(digit) * (base ** place) for place, digit \
              in enumerate(reversed(i))])
    n += sum([int(digit) * (base ** -place) for place, digit \
              in enumerate(f)])
    if negative: n = -n
    return n

if __name__ == '__main__':
    print('|'.join(("dec.".ljust(5), "e".ljust(9), "to 10".ljust(6), \
                    "error".ljust(6), "digits")))
    for i in range(-10, 20):
        digits = to_digits(i)
##        print(digits)
        decimal = to_10(*digits)
        error = decimal - i
        print('|'.join(\
            (str(i).rjust(4) + ':', \
              str(eBase(i)).rjust(9), \
              "{:.2f}".format(decimal).rjust(6), \
              "{:.2f}".format(error).rjust(6), \
              " dummy")))

##>>> n = 10
##>>> n
##10
##>>> digits = []
##>>> digits
##[]
##>>> for i in reversed(range(power+1)):
##	d, n = divmod(n, e**i)
##	digits.append((d, i))
##	print(digits)
##
##	
##[(1.0, 2)]
##[(1.0, 2), (0.0, 1)]
##[(1.0, 2), (0.0, 1), (2.0, 0)]
##>>> n
##0.6109439010693505
##>>> for i in range(10):
##	d, n = divmod(n*e, e)
##	digits.append((d, -i-1))
##	print(digits)
##
##	
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4), (0.0, -5)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4), (0.0, -5), (1.0, -6)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4), (0.0, -5), (1.0, -6), (0.0, -7)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4), (0.0, -5), (1.0, -6), (0.0, -7), (1.0, -8)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4), (0.0, -5), (1.0, -6), (0.0, -7), (1.0, -8), (1.0, -9)]
##[(1.0, 2), (0.0, 1), (2.0, 0), (0.0, -1), (1.0, -2), (1.0, -3), (2.0, -4), (0.0, -5), (1.0, -6), (0.0, -7), (1.0, -8), (1.0, -9), (1.0, -10)]

##for acc in range(100):
##    num = to_10(*to_digits(n, acc))
##    a, b = b - num, num
##    print(acc, 26, num, 26 - num, a)
