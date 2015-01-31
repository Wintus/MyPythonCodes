#Calc primes

#calc the list of primes
def prime(n):
    ps=[2,3]
    for i in range(3,n):
        if i%6==1 or i%6==5:
            for p in ps:
                if i%p==0:
                    break
                else:
                    ps.append(i)
            
    print("There are {1} pirmes up to {2}.\nThe list of primes: {0}".format(ps, len(ps), n))

def main():
    n = eval(input("Primes up to "))
    prime(n)

main()
