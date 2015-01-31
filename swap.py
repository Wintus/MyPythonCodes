# Python 3.4.0

'''Swap the values of a and b without any extra variables'''

# use tuple in assignment (basic version)
a, b = 0, 1
print("a: {}, b: {}".format(a, b))
print("Swapping")
a, b = b, a
print("a: {}, b: {}".format(a, b))
print()

# with closure (it seems same with above one essentially)
def main():
    '''use closure to swap'''
    a, b = 0, 1
    def swap():
        nonlocal a, b
        a, b = b, a
        print("Swapped")
        return a, b
    print("a: {}, b: {}".format(a, b))
    swap()
    print("a: {}, b: {}".format(a, b))
    print()

main()

# use function
def swap(a, b):
    '''swap a and b'''
    print("Swapping")
    return b, a
a, b = 0, 1
print("a: {}, b: {}".format(a, b))
a, b = swap(a, b)
print("a: {}, b: {}".format(a, b))
print()

# apply reversed() on the sequence
a, b = 0, 1
print("a: {}, b: {}".format(a, b))
a, b = reversed( (a, b) )
print("a: {}, b: {}".format(a, b))
print()

# use reference
a, b = 0, 1
print("a: {}, b: {}".format(a, b))
a, b = (a, b)[1], (a, b)[0]
print("a: {}, b: {}".format(a, b))
print()
