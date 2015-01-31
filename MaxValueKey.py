'''Get the key with the maximum value in a dictionary'''

def max_value_key(dic):
    '''dic -> key (of the max value)

    Ex. dic = {'A':1, 'B':2, 'C':3} -> ('C', 3)[0]'''
    return max(dic.items(), key = lambda x: x[1])[0]
