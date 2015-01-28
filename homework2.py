"""This program determines the cost of 3 items with taxes and shipping fees."""

def order_calculator():
    """The main function.

    This function gets 3 inputs of items.
    Each line of inputs consists of
        description, price, quantity, weight per item.
    Then, it display the items, SubTotal, Tax, Shipping costs, and the Total.
    Success: () -> __Finished__ | () -> __ERROR__"""

    #Literals
    ship_rate = .25 #($/lb)
    handling_charge = 5.0 #per order
    tax = 8.5 / 100 #% to rate

    #Each item is represented by a dictoinary type
##    dic_item = {"id":0, "name":"dummy",\
##                "price":0.0, "quantity":0, "weight":0.0}
    #list_items is a list of dictionaries like dic_item
    print("Enter your order of each items.")
    print("Inputs should follow the format: " + \
          "Description Price Quantity Weight(in pounds)")
    print("Enter nothing to proceed to cashing.")
    #Make a order list of items
    list_items = []
    list_input = []
    count = 0
    while True:
        item = dict()
            #Initialize by creating a new dictionary because of the reference
        list_input = input("Enter the item No.{}: ".format(count+1)).split()
        if list_input == []:
            print("> Proceed to cashing\n")
            break
        #Input values into the 'n'th dictionary in the item list
        try: #Error check
##            item["id"]      = int(count)
            item["name"]    = str(list_input[0])
            item["price"]   = float(list_input[1])
            item["quantity"]= int(list_input[2])
            item["weight"]  = float(list_input[3])
            list_items.append(item)
            #Show the last inputed item
            print("> {} ${:,.2f} {:,} each {:,.1f}lbs\n"\
                  .format(item["name"], item["price"],\
                          item["quantity"], item["weight"]
                          )
                  )
            count += 1
        except IndexError:
            print("Lack of value")
            print("Please Input all required information.\n")
        except ValueError:
            print("Invalid value")
            print("Input information correctly.\n")
        except:
            print("UNKNOWN ERROR")
            return "__ERROR__"

    #Skip when the order is empty
    if list_items == []:
        print("You purchased nothing. End the order.")
        return "__Finished__"

    #Calculate the costs
##    total = 0.0
##    subtotal = 0.0
##    total_weight = 0.0

    #Calc the subtotal, the total weight, the tax,
        #and the shipping and handling cost
    
    def zipWith_each_items(func, list_of_items, key1, key2):
        """Multiple 2 value of the 2 given keys"""
        return sum(map(lambda dic1, dic2 : func(dic1[key1], dic2[key2]),\
##                       list_of_items, list_of_items))
                       *([list_of_items] * 2))) #Omit the duplicate

    def multi(a, b):
        """Multiply"""
        return a * b
    
    subtotal = zipWith_each_items(multi, list_items, "price", "quantity")
    total_weight = zipWith_each_items(multi, list_items, "weight", "quantity")

    #Tax
    items_tax = subtotal * tax
    #Shipping and Handling costs
    ship_handl = ship_rate * total_weight + handling_charge

    #Sums up subtotal, tax, shipping fee and handling charge
    total = subtotal + items_tax + ship_handl
    
    #Display the order
    
    #Define modifier functions
    def insert_last_and(list_str): # [str] -> [str]
        """Combine last 2 strings with ' and '

    Ex. ['a', ... , 'y', 'z'] -> ['a', ... , 'y and z']"""
        if len(list_str) == 1: return list_str # for more than 1
        last_two = " and ".join(list_str[-2:])
            #Slice out the lest 2 and join them with ' and '
        return list_str[:-2] + [last_two]

    def plural_form(n, str_thing):
        """Support modifying singleton, plural form

    Ex. 1 -> (1, thing) | int n -> (n, thing's') | ERROR"""
        if n == 1:
            return (n, str_thing)
        elif type(n) == type(1):
            return (n, str_thing + 's')
        else:
            return ValueError

    #Print the order
    print("You have purchased {} {}: ".format(*plural_form(count, 'item')) + \
          ', '.join( # [<str>] -> <str>
              insert_last_and([item["name"] for item in list_items])
                  #Use list comprehention of making a list of item descriptions
                    ) + '.'
          )
    print("The subtotal is ${:,.2f}.".format(subtotal))
    print("The Shipping and Handling costs are ${:,.2f}.".format(ship_handl))
    print("The Tax is ${:,.2f}.".format(items_tax))
    print("The Total is ${:,.2f}.".format(total))
    return '__Finished__'

if __name__ == '__main__': #Run only in a direct call
    order_calculator()

    #Sample Imput:
    #Shovel $25.00 1 each 6lbs
    #Planter $45.00 2 each 11lbs
    #Broom $12.00 1 each 4lbs
    
    #Sample Output:
    #You have purchased: Shovel, Planter and Broom.
    #The subtotal is $127.00
    #The Shipping and Handling costs are $13.00
    #The Tax is $10.795 ($11.90)
    #The Total is $150.795 ($151.90).
