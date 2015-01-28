# continued fraction

from math import modf

def cf(p):
    cflist=[]
    e=.1**5
    while True:
        p, q = modf(p)
        #print(int(q), '+', p)
        cflist.append(int(q))
        if p<e:
            break
        else:
            p=1/p

    return cflist

def main():
    print("Convert a number into a list of conitnued fraciton.")
    p = input("Enter a number: ")
    print(cf(float(p)))

main()
