# Project:      Template (MaemichiYuyaHomework03Sec01.py)
# Name:         Yuya Maemichi
# Date:         05/14/14
# Description:  This program determines the cost of sending out coffee.

def coffee_price(strOrder, fltPounds):
    '''calc the coffee price'''
    fltJB = 10.50 # $/lbs - Jonestown Brew
    fltPJ = 16.95 # $/lbs - Plymouth Jolt
    if strOrder == 'J':
        return fltJB * fltPounds
    elif strOrder == 'P':
        return fltPJ * fltPounds
    else:
        raise ValueError

def tax(fltAmount, strState):
    '''calc the tax'''
    if strState == 'WA' or 'CA' or 'TX':
        return fltAmount * .09
    elif strState == 'OR' or 'FL':
        return fltAmount * .00
    elif len(strState) == 2:
        return fltAmount * .07
    else:
        raise ValueError

def shipping_and_handling_cost(fltPounds, strOption):
    '''calc the shipping and handling cost'''
    fltShippingRate = 0.93 # $/lbs
    fltHandlingCost = 2.50 # $/order
    if strOption == 'O':
        fltShipping = 20.00
    elif strOption == '2':
        fltShipping = 13.00
    elif strOption == 'S':
        fltShipping = 0.00
    else:
        raise ValueError
    fltShipping += fltShippingRate * fltPounds + fltHandlingCost
    return fltShipping

def payment(fltSubtotal, intOption):
    '''calc the amount at the payment'''
    # 0:Cash, 1:PayPal, 2:Credit Cards, 3:Check
    if intOption == 1:
        intRate = 3 # PayPal
    elif intOption == 2:
        intRate = 5
    elif intOption == 3:
        intRate = -2
    else:
        intRate = 0
    return fltSubtotal * (1 + intRate / 100)

def main():
    '''the main function'''
    print("Coffee shop")
       
    while True:
        try:
            fltTotal = 0.0

            # get inputs and calculate
            # coffee
            print("Jonestown Brew: J, Plymouth Jolt: P")
            strCoffee = str(input("Coffee?: ")).upper()
            if not strCoffee:
                raise ValueError("Empty input")
            elif strCoffee == 'J':
                strCoffeeName = "Jonestown Brew"
            elif strCoffee == 'P':
                strCoffeeName = "Plymouth Jolt"
            else:
                raise ValueError("Invalid input")
            print('>', strCoffeeName)
            print()
            fltPounds = float(input("Amount? (lbs): "))
            print('>', fltPounds)
            fltCoffeePrice = coffee_price(strCoffee, fltPounds)
            print()

            # city and state
            print("Enter the City and State for shipping")
            strCity = str(input("City?: ")).title()
            strState = str(input("State?: ")).upper()
            print('>', strCity)
            print('>', strState)
            print()

            # shiping method
            print("Overnight: O, 2-Days: 2, Standard:, S")
            strOption = str(input("Shipping method?: ")).upper()
            print('>', strOption)
            fltShipping = shipping_and_handling_cost(fltPounds, strOption)
            fltSubtotal = fltCoffeePrice + fltShipping
            # tax
            fltTax = tax(fltSubtotal, strState)
            print()

            # payment option
            print("0:Cash, 1:PayPal, 2:Credit Cards, 3:Check")
            intOption = int(input("Payment option?: "))
            options = ("cash", "PayPal", "Credit Cards", "Check",)
            print('>', options[intOption])
            print()

            fltTotal = fltSubtotal + payment(fltTotal, intOption) + fltTax
            fltTotal = round(fltTotal, 2)

            # display the order
            print("YOUR ORDER")
            print("Coffee:", strCoffeeName)
            print("Amount: {:.2f}lbs.".format(fltPounds))
            print("Coffee price: {:.2f}".format(fltCoffeePrice))
            print("Shipping & Handling costs: {:.2f}".format(fltShipping))
            print("Subtotal: {:.2f}".format(fltSubtotal))
            print("City:", strCity)
            print("State:", strState)
            if strOption == 'O':
                print("Shipping method: Overnight")
            elif strOpiton == '2':
                print("Shipping method: 2-Days")
            elif strOption == 'S':
                print("Shipping method: Standard")

            if intOption == 1:
                print("Payment option: PayPal")
            elif intOption == 2:
                print("Payment option: Credit Cards")
            elif intOption == 3:
                print("Payment option: Check")
            else:
                print("Payment option: Cash")
            print("Tax: {:.2f}".format(fltTax))
            print("Total:", fltTotal)
            
            print()
            break
        
        except ValueError:
            print("Please input correctly")
            print()

    print("Thank you for shopping")
    

if __name__ == '__main__': #run only in a direct call
    main()
