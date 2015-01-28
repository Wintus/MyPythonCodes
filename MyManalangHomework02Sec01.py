# Project:      Homework 02 (MaemichiManalangHomework02Sec01.py)
# Name:         Maemichi, Yuya & Martina Manalang
# Date:         04/28/14
# Description:  This program will allow the user enter information about 3 items and receive their subtotal, tax, shipping and handling and total.

def main():
    strDescription = ""
    intSubtotal = 0
    intTotalWeight = 0
    intShipping = 0
    intTax = 0
    
    for i in range(3):
       strPurchase = str(input("Please enter the item description: "))
       intPrice = int(input("PLease enter the price:  $"))
       intQuantity = int(input("Please enter the quantity: "))
       intInitialWeight = int(input("Please enter the weight per item(lbs): "))

       strDescription += strPurchase + ", "

       intTotalWeight += intInitialWeight

       intSubtotal += (intPrice * intQuantity)

       intShipping += (.25 * (intInitialWeight * intQuantity))

       intTax += .085 * (intPrice * intQuantity)

    intShipping += 5 # HC
    intTotal = intSubtotal + intShipping + intTax


    print("You have purchased:", strDescription)
    print("The subtotal is $", intSubtotal)
    print("The Shipping and Handling costs are $", intShipping)
    print("The Tax is ${0:0.2f}".format(intTax))
    print("The Total is ${0:0.2f}".format(intTotal))


main()

