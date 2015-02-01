# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from itertools import takewhile, izip

# longest common prefix
def lcp(s0, s1):
    def all_eq(x):
        return len(set(x)) == 1
    i = len(tuple(takewhile(all_eq, izip(s0, s1))))
    return s0[:i+1]

m, n = map(int,raw_input().split())
wakas = [raw_input() for i in xrange(m)]

def kimali(s, l=wakas):
    ks = [lcp(s,w) for w in wakas if s != w]
    return max(ks, key=len)

kimalis = [kimali(w) for w in wakas]

print kimalis[n-1]

##9 3
##kirigirisunakuyashimoyonosamushironi
##kimigatameharunononiidetewakanatsumu
##chihayaburukamiyomokikazutatsutagawa
##ookotonotaeteshinakuwanakanakani
##ooeyamaikunonomichinotokereba
##ookenakuukiyonotaminioukana
##chigiriokishisasemogatsuyuoinochinite
##kimigatameoshikarazarishiinochisae
##chigirikinakataminisodeoshiboritsusu
##
##=> chih
