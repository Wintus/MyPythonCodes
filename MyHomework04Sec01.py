# Project:      Template (MaemichiYuyaHomework03Sec01.py)
# Name:         Yuya Maemichi
# Date:         05/14/14
# Description:  This program determines the cost of sending out coffee.

def coffee_price(order, lbs=0.0):
    '''calc the coffee price'''
    fltJB = 10.50 # $/lbs - Jonestown Brew
    fltPJ = 16.95 # $/lbs - Plymouth Jolt
    coffee = {"Jonestown Brew":10.05, "Plymouth Jolt":16.95,}
    return coffee[order] * lbs

def tax(amount, region="the Others"):
    '''calc the tax'''
    taxes = {"Washington":9, "California":9, "Texas":9, \
             "Oregon":0, "Florida":0, 'the Others':7,}
    return amount * (1 + taxes[region] / 100)

def shipping_and_handling_cost(lbs, option="Standard"):
    '''calc the shipping and handling cost'''
    fltShippingRate = 0.93 # $/lbs
    fltHandlingCost = 2.50 # $/lbs
    shipping_methods = {"Overnight":20.00, "2-Day":13.00, "Standard":0.00,}
    return fltShippingRate * lbs + fltHandlingCost + \
           shipping_methods[option]

def payment(subtotal, option="cash"):
    '''calc the amount at the payment'''
    options = {"Paypal":3, "Credit Cards":5, "Check":-2, "cash":0,}
    return subtotal * (1 + options[option] / 100)

##def counter(total, func, arg):
##    total += round(func, total, arg)

def main():
    '''the main function'''
    print("Coffee shop")
##    finished = False
    total = 0.0

    def interface(func, dic, key, prompt):
        '''Abstraction of repeated patterns'''
        nonlocal total
        print(prompt)
        arg = dic[key]
        print('>', arg)
        total += func(total, arg)
        print()
        
##    while not finished:
    while True:
        try:
            total = 0.0

            coffees = {'J':"Jonestown Brew", 'P':"Plymouth Jolt",}            
            print("Jonestown Brew: J, Plymouth Jolt: P")
            coffee = str(input("Coffee?: ")).upper()
            print('>', coffees[coffee])
            print()
            lbs = float(input("Amount? (lbs): "))
            print('>', lbs)
            total += coffee_price(order, lbs)
            print()

            region = str(input("Region?: ")).upper()
            states = {'W':"Washington", 'C':"California", 'T':"Texas", \
                      'O':"Oregon", 'F':"Florida", '':"the Others",}
            print('>', states[region])
            total += tax(total, states[region])
            print()

            option = int(input("Payment method?: "))
            options = ("cash", "Paypal", "Credit Cards", "Check",)
            print('>', options[option])
            total += payment(total, options[option])
            print()

            method = str(input("Shipping option?: ")).upper()
            methods = {'O':"Overnight", '2':"2-Day", 'S':"Standard",}
            print('>', methods[method])
            total += shipping_and_handling_cost(lbs, methods[method])
            print()

            total = round(total, 2)
            print("Total:", total)
            print()
##            finished = True
            break
        
        except ValueError:
            print("Please input correctly")

    print("Thank you for shopping")
    

if __name__ == '__main__': #run only in a direct call
    main()
