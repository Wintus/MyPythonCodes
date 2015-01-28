def main():
    strDescription = ""
    intSubtotal = 0
    
    
    for i in range(3):
       strPurchase = str(input("Please enter the item description:"))
       intPrice = int(input("PLease enter the price: $"))
       intQuantity = int(input("Please enter the quantity:"))
       intWeight = int(input("Please enter the weight per item(lbs):"))

       strDescription = strDescription + " " + strPurchase

       intSubtotal = intSubtotal + (intPrice * intQuantity)

       intShipping = (.25 * (intWeight * intQuantity))+ 5

       intTax = .085 * (intSubtotal + intShipping)

       intTotal = intSubtotal + intShipping + intTax


    print("You have purchased:", strDescription)
    print("The subtotal is $", intSubtotal)
    print("The Shipping and Handling costs are $", intShipping)
    print("The Tax is $", intTax)
    print("The Total is $", intTotal)


main()

