#Calc primes

#calc the list of primes up to 2^n
def prime(n):
    ps=[2,3]
    for i in range(3,2**n):
        if i%6==1 or i%6==5:
            for p in ps:
                if i%p==0:
                    break
                ps.append(i)
            
    print("There are {1} pirmes up to {2}.\nThe list of primes: {0}".format(ps, len(ps), 2**n))

def main():
    n = eval(input("Primes up to 2 ^ "))
    prime(n)

main()
