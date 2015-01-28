# Project:	2 numbers x 6 lines Program (MaemichiYuyaHomework01Sec01'.py)
# Name:	        Yuya Maemichi
# Date:		04/15/14
# Description: 	This program gets numbers and show them 6 times.

def main():
    # get 2 or more numbers and put them into a list
    nlist = list(map(int, input("Imput two numbers: ").split()))
    # print(nlist)

    # print 2 numbers 6 times
    for i in range(6):
        print("{0} {1}".format(nlist[0], nlist[1]))

main()
