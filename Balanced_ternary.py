def val(number_sequence, base):
    """ produce integer value of number_sequence as base number """
    return sum(int(n) * base ** p\
               for p, n in enumerate(reversed(number_sequence)))

def balanced_ternary_value(number):
    """ produce integer value of balanced ternary number """
    return val([(-1 if c == 'T' else (1 if c == '1' else 0))\
                for c in str(number)], 3)

def make_balanced(n):
    """ Make balanced ternary by doing carry at
    2 and using identity 2 = 3 + -1
    """
    n = int(n)
    if not n:
        return '0'
    else:
        digits = ''
        while n:
            n, this = divmod(n, 3)
            if this == 2:
                n += 1
            digits = '01T'[this] + digits
    return digits

class BalancedTernary:
    def __init__(self, num):
        if isinstance(num, int):
            self.num = num
        elif isinstance(num, str):
            self.num = balanced_ternary_value(num)
        else:
            raise ValueError('Invalid argument')
        
##    def __new__(cls, n):
##        instance = num.__new__(cls, balanced_ternary_value(n)\
##                               if isinstance(n, str) else n)
##        return instance

##    def __call__(self, n):
##        if isinstance(n, str):
##            return balanced_ternary_value(n)
##        else:
##            return n
       
    def __repr__(self):
        return make_balanced(self.num)
    __str__ = __repr__

    
if __name__  == '__main__':
    print(('%10s %10s' % ('dec', 'balanced ternary')))
    for t in range(-27,+28):
        print(('%10s %10s' % (t, BalancedTernary(t))))
        assert balanced_ternary_value(str(BalancedTernary(t))) == t
    print(balanced_ternary_value('11T01'))
    print(BalancedTernary(100), BalancedTernary('11T01').num)
    bt = BalancedTernary(100)
    print(bt, bt.num)
