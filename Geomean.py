'''calculate geomean avoiding overflow'''
from math import log10 as log10

def geomean(ns):
    log_list = [log10(n) for n in ns]
    log_avg  = sum(log_list) / len(ns)
    return pow(10, log_avg)

### bad
##def geomean(ns):
##    n = len(ns)
##    multi = 1.0
##    for i in range(n):
##        multi *= ns[i]
##    return pow(multi, 1/n)
