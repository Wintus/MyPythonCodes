"""This program determines the cost of 3 items with taxes and shipping fees."""

def order_calculator():
    """The main function.

    This function gets 3 inputs of items.
    Each lines of inputs consists of
    description, price, quantity, weight per item.
    Then it display the items, SubTotal, Shipping costs, the Tax, and the Total."""

    #literals
    ship_rate = .25 #($/lb)
    handling_charge = 5.0 #per order
    tax = 8.5/100 #% in rate

    #Sample Imput:
    #Shovel $25.00 1 each 6lbs
    #Planter $45.00 2 each 11lbs
    #Broom $12.00 1 each 4lbs
    item_numbers = 3 #static
    list_items = list(range(item_numbers)) #hash is preferable
    print("Enter the order of {} items.")
    print("Inputs should follow the format: Description Price Quantity Weight(in pounds)")
    #Make a order list of items
    for i in range(item_numbers):
        list_items[i] = input("Enter the item No.{}: ".format(i+1)).split()
        print("> {} ${:.2f} {} each {}lbs\n"\
              .format(str(list_items[i][0]), float(list_items[i][1]),\
                      int(list_items[i][2]), int(list_items[i][3])))

    #Calculate the costs
    total = 0.0
    subtotal = 0.0
    total_weight = 0.0
    #total_items = item_numbers # == 3
    
    for i in range(item_numbers):
        subtotal += float(list_items[i][1]) * int(list_items[i][2])

    for i in range(item_numbers):
        total_weight += int(list_items[i][2]) * float(list_items[i][3])

    #sums up subtotal, shipping fee, handling charge, and tax
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
    #The Tax is $11.90 
    #The Total is $151.90.
    print("You have purchased: {}, {}, and {}."\
          .format(list_items[0][0], list_items[1][0], list_items[2][0]))
    print("The subtotal is ${:.2f}.".format(subtotal))
    print("The Shipping and Handling costs are ${:.2f}."\
          .format(ship_handl))
    print("The Tax is ${:.2f}.".format(items_tax))
    print("The Total is ${:.2f}.".format(total))

order_calculator()
