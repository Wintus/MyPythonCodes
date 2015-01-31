'''Negative base'''

class NegativeBase():
    '''Super class for negative bases

    base <= -2'''

    str_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, base, n):
        if not base < -1:
            raise ValueError('Base should be "base <= -2"')
        self.base = base
        self.num = self.initializer(n)
##        self.digits_list = tuple(range(-base))

    def initializer(self, x):
        '''x: int | str

    Return: int'''
        if isinstance(x, int):
            return x
        elif isinstance(x, str):
            return self.to_decimal(x)
        else:
            raise ValueError('Invalid argument')

    def to_digits(self, n):
        digits = ''
        if not n:
            digits = '0'
        else:
            while n:
                n, remainder = divmod(n, self.base)
                if remainder < 0:
                    n, remainder = n + 1, remainder + (-self.base)
                digits = str(self.str_digits[remainder]) + digits
        return digits

    def to_decimal(self, digits):
        return sum([(self.str_digits.find(digit) * (self.base ** place)) \
                    for place, digit in enumerate(reversed(digits))])

    def __repr__(self):
        return self.to_digits(self.num)
    __str__ = __repr__

    def __int__(self):
        return self.num

    def __add__(self, y):
        z = int(self) + int(y)
        return NegativeBase(self.base, z)

    def __radd__(self, x):
        Z = int(x) + int(self)
        return NegativeBase(self.base, z)

    def __sub__(self, y):
        z = int(self) - int(y)
        return NegativeBase(self.base, z)

    def __rsub__(self, x):
        z = int(x) - int(self)
        return NegativeBase(self.base, z)


class Negabinary(NegativeBase):
    '''base: -2'''
    def __init__(self, n):
        '''initialized in both int and str'''
        NegativeBase.__init__(self, -2, n)

##    def negabinary(self, n):
##        digits = ''
##        if not n:
##            digits = '0'
##        else:
##            while n:
##                n, remainder = divmod(n, self.base)
##                if remainder < 0:
##                    n, remainder = n + 1, remainder + (-self.base)
##                digits = str(remainder) + digits
##        return digits
##
##    def __repr__(self):
##        return self.negabinary(self.num)


class Negaternary(NegativeBase):
    '''base: -3'''
    def __init__(self, n):
        '''initialized in both int and str'''
        NegativeBase.__init__(self, -3, n)

##    def negaternary(self, n):
##        digits = ''
##        if not n:
##            digits = '0'
##        else:
##            while n:
##                n, remainder = divmod(n, self.base)
##                if remainder < 0:
##                    n, remainder = n + 1, remainder + (-self.base)
##                digits = str(remainder) + digits
##        return digits
##
##    def __repr__(self):
##        return self.negaternary(self.num)


class Negadecimal(NegativeBase):
    '''base: -10'''
    def __init__(self, n):
        NegativeBase.__init__(self, -10, n)

        
if __name__ == '__main__':
    print("Decimal", "Negabinary", "Negaternary", "Negadecimal")
    for i in range (-10, 20):
        print(str(i).rjust(7), str(Negabinary(i)).rjust(10), \
              str(Negaternary(i)).rjust(11), str(Negadecimal(i)).rjust(11))
