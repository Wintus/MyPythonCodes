# Project:      Homework 02 (MaemichiManalangHomework02Sec01.py)
# Name:         Maemichi, Yuya & Martina Manalang
# Date:         04/28/14
# Description:  This program will allow the user enter information about 3 items and receive their subtotal, tax, shipping and handling and total.

def main():
    strDescription = []
    fltSubtotal = 0.0
    fltShipping = 0.0
    
    for i in range(3):
       strDescription += [str(input("Please enter the item description: "))]
       fltPrice = float(input("PLease enter the price: $"))
       intQuantity = int(input("Please enter the quantity: "))
       fltWeight = float(input("Please enter the weight per item(lbs): "))

       fltSubtotal += fltPrice * intQuantity
       fltShipping += .25 * fltWeight * intQuantity

    fltShipping += 5 #Handling charge
    fltTax = .085 * fltSubtotal
    fltTotal = fltSubtotal + fltTax + fltShipping

    print()
    print("You have purchased: {}, {} and {}.".format(*strDescription))
    print("The subtotal is ${}.".format(fltSubtotal))
    print("The Shipping and Handling costs are ${}.".format(fltShipping))
    print("The Tax is ${:.2f}.".format(fltTax))
    print("The Total is ${:.2f}.".format(fltTotal))


main()

