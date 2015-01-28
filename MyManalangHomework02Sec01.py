# Project:      Homework 02 (MaemichiManalangHomework02Sec01.py)
# Name:         Maemichi, Yuya & Martina Manalang
# Date:         05/01/14
# Description:  This program will allow the user enter information of 3 items
#   and display their subtotal, tax, shipping and handling cost, and total.

def main():

    #Initialize accumulators
    strDescription = []
##    strDescription = "" # string accumulator version
    fltSubtotal = 0.0
    fltShipping = 0.0

    #Error checking
    try:
        for i in range(3):
            #Get user inputs
           strDescription += [str(input("Please enter the item description: "))]
##           strName = str(input("Please enter the item descirption: "))
           fltPrice = float(input("PLease enter the price: $"))
           intQuantity = int(input("Please enter the quantity: "))
           fltWeight = float(input("Please enter the weight per item(lbs): "))

           #Accumulating
##           strDescription += strName + ' ' #string accumulator version
           fltSubtotal += fltPrice * intQuantity
           fltShipping += .25 * fltWeight * intQuantity
    except ValueError:
        #Check the wrong input like casting a string into int() or float()
        print("ERROR: Wrong Inputs captured")
        return '__ERROR__'

    #Process the rest of values
    fltShipping += 5 #Handling charge
    fltTax = .085 * fltSubtotal
    fltTotal = fltSubtotal + fltTax + fltShipping

    #Display the result
    try:
        print()
        #I couldn't make this out without using *. -- Yuya
        #But I think it's a tiny difference.
        #I also have a string version below.
        print("You have purchased: {}, {} and {}.".format(*strDescription))
##        print("You have purchased:", strDescription)
        
        print("The subtotal is ${}.".format(fltSubtotal))
        print("The Shipping & Handling is ${}.".format(fltShipping))
        print("The Tax is ${:.2f}.".format(fltTax))
        print("The Total is ${:.2f}.".format(fltTotal))
    except:
        #This program should be quited before getting here by former return.
        print("UNKNOWN ERROR: Something goes wrong.")
        return '__ERROR__'

main()

#Sample inputs
##Please enter the item description: a
##PLease enter the price: $1
##Please enter the quantity: 2
##Please enter the weight per item(lbs): 3
##Please enter the item description: b
##PLease enter the price: $4
##Please enter the quantity: 5
##Please enter the weight per item(lbs): 6
##Please enter the item description: c
##PLease enter the price: $7
##Please enter the quantity: 8
##Please enter the weight per item(lbs): 9

#Sample outputs
##
##You have purchased: a, b and c.
##The subtotal is $78.0.
##The Shipping and Handling costs are $32.0.
##The Tax is $6.63.
##The Total is $116.63.

#Output check by calculator -- Yuya Maemichi
