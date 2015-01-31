'''Permutation'''

import TailRecursive

result, perm = [], []
def make_perm0(n, m = 0):
##    result, perm = [], []
    if n == m:
        result.append(perm)
    else:
        for x in range(1, n + 1):
            if x in perm:
                continue
            perm.append(x)
            make_perm0(n, m + 1)
            perm.pop()
##        return result

