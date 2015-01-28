def qs(l):
    """ quick sort function """
    if len(l) == 0:
        return l
    return qs([x for x in l[1:] if x < l[0]]) + [l[0]] \
               + qs([x for x in l[1:] if x >= l[0]])
