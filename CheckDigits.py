# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def findX(n):
    n0 = str(n)[0:15]
    ns = [n0 + str(i) for i in xrange(10)]
    
    def isValid(digits):
        def sum_digits(str_n, even=True):
            digits = map(int, str_n)
            if (even):
                digits = map(lambda n: sum(divmod(n,10)),
                    map(lambda n: n * 2, digits))
            return sum(digits)
        even = sum_digits(digits[1::2])
        odd = sum_digits(digits[::2], even=False)
        return (even + odd) % 10 == 0
    for n in ns:
##        print isValid(n), n
        if (isValid(n)):
            return n[-1]

if __name__ == '__main__':
    n = int(raw_input())
    nums = [raw_input() for i in xrange(n)]
    for n in nums:
        print findX(n)
