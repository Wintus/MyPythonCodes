"""This program determines the cost of 3 items with taxes and shipping fees."""

def order_calculator():
    """The main function.

    This function gets 3 inputs of items.
    Each lines of inputs consists of
    description, price, quantity, weight per item.
    Then it display the items, SubTotal, Shipping costs, the Tax, and the Total."""

    #Literals
    ship_rate = .25 #($/lb)
    handling_charge = 5.0 #per order
    tax = 8.5 / 100 #% in rate

    #Sample Imput:
    #Shovel $25.00 1 each 6lbs
    #Planter $45.00 2 each 11lbs
    #Broom $12.00 1 each 4lbs
    
##    item_number = 3 #static, no use now
    #Each item is represented by a dictoinary
##    dic_item = {"id":0, "name":"dummy", "price":0.0, "quantity":0, "weight":0.0}
    #list_items is a list of dictionaries
    list_items = [] # [dic_item] * item_number
    print("Enter your order of each items.")
##          .format(item_number))
    print("Inputs should follow the format:",\
          "Description Price Quantity Weight(in pounds)")
    print("Enter nothing to proceed to cashing.")
    #Make a order list of items
    list_input = []
    count = 0
    while True:
##    for i in range(item_number):
        item = dict() #create a new dictionary because of the reference
        list_input = input("Enter the item No.{}: ".format(count+1)).split()
        if list_input == []:
            print()
            break
        #Input values into 'i'th dictionary
        try:
            item["id"] = int(count)
            item["name"] = str(list_input[0])
            item["price"] = float(list_input[1])
            item["quantity"] = int(list_input[2])
            item["weight"] = float(list_input[3])
            list_items.append(item)
            #Show last inputed item
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
##        except:
##            print("UNKNOWN ERROR")
##            return "__ERROR__"
##        print(list_items)

    #Skip when the order is empty
    if list_items == []:
        print("You purchased nothing. End the order.")
        return "__Finished__"
##    print("\n>",list_items,"\n")

    #Calculate the costs
    total = 0.0
    subtotal = 0.0
    total_weight = 0.0
##    total_items = item_number # == 3

    #Loop that depends on i
##    for i in range(item_number):
##        subtotal += list_items[i]["price"] * list_items[i]["quantity"]
##        #print(subtotal)
##        total_weight += list_items[i]["weight"] * list_items[i]["quantity"]
##        #print(total_weight,"\n")

    #The following messy code fragment was expected to work as well as above loop
##    for i in range(item_number):
##        subtotal, total_weight =\
##            [total + value1 for (total, value1) in\ #list comprehension
##                zip((subtotal, total_weight),\ #<(subt.,grospri.),(t._w.,grosw.)>
##                    [value0 * list_items[i]["quantity"] for value0 in\
##                        (list_items[i]["price"], list_items[i]["weight"])
##                     ]
##                    )
##             ]#Alternative to zipWith(2)
##        #map = zipWith1
    
##    _subtotal = sum(map(lambda dic1, dic2: dic1["price"] * dic2["quantity"],\
##                       list_items, list_items))
##    print(_subtotal)
##    _total_weight = sum(map(lambda dic1, dic2: dic1["weight"] * dic2["quantity"],\
##                       list_items, list_items))
##    print(_total_weight)

    #Clac the subtotal and the total weight
    def zip_each_item(list_of_items, key1, key2):
        return sum(map(lambda dic1, dic2 : dic1[key1] * dic2[key2],\
                       list_of_items, list_of_items))
    subtotal = zip_each_item(list_items, "price", "quantity")
##    print(_subtotal)
    total_weight = zip_each_item(list_items, "weight", "quantity")
##    print(_total_weight)

    #Sums up subtotal, shipping fee, handling charge, and tax
    #subtotal
    total += subtotal
    #Tax
    items_tax = subtotal * tax
    total += items_tax
    #Shipping and Handling costs
    ship_handl = ship_rate * total_weight + handling_charge
    total += ship_handl
    
    #Display the order
    
    #Sample Output:
    #You have purchased: Shovel, Planter and Broom.
    #The subtotal is $127.00
    #The Shipping and Handling costs are $13.00
    #The Tax is $10.79 ($11.90)
    #The Total is $150.79 ($151.90).

##    print("You have purchased: {}, {}, and {}."\
##          .format(list_items[0]["name"], list_items[1]["name"],\
##                  list_items[2]["name"]
##                  )
##          )
    #Use list comperehension to shorten the statement
##    print(tuple([item["name"] for item in list_items]))
##    print("You have purchased: {}, {}, and {}."\
##          .format(*[item["name"] for item in list_items])) #need * to read it
    #Adopt to muliple items more than 3

    #Define a function to modify a serise of strings
    def insert_last_and(list_str): # [str] -> [str]
        if len(list_str) == 1: return list_str
        last_list_str = list_str[-1:]
        #Add "and " on the head of the last
        last_list_str = list(map(lambda s : "and " + s, last_list_str))
        return list_str[:-1] + last_list_str

    #Define a funciton to modify singleton
    def singl_s(n):
        if n == 1:
            return (n, '')
        elif type(n) == type(1):
            return (n, 's')
        else:
            return ValueError

    #Print the order
    print("You have purchased {0} item{1}: ".format(*singl_s(count)) + \
          ', '.join(insert_last_and(
                    [item["name"] for item in list_items] # [<str>] -> <str>
                                    )
                    ) + '.'
          )
    print("The subtotal is ${:.2f}.".format(subtotal))
    print("The Shipping and Handling costs are ${:,.2f}.".format(ship_handl))
    print("The Tax is ${:,.2f}.".format(items_tax))
    print("The Total is ${:,.2f}.".format(total))

if __name__ == '__main__':
    order_calculator()
