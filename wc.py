# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from operator import add

command = raw_input()
n = int(raw_input())
strs = [raw_input() + ' ' for i in xrange(n)]
words = reduce(add, [s.split() for s in strs])

##print strs, words

if command == 'w':
    print len(words)
elif command == 'c':
    print len(''.join(strs))
else:
    print len(words)
    print len(''.join(strs))
