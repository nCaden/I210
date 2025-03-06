# 12.1 Pizza order

def order_pizza_original(size, crust, sauce, topping):
    """Confirms a pizza order"""
    print("One", size, crust, "crust pizza with", sauce, "sauce, topped with", topping + ".")


# (A) To save time for your employees typing in an order, as most customers order 
# a thin crust with red sauce, and only one topping choice, make these the defaults!
# write function here

def order_pizza(size, topping, sauce = "red", crust = "thin", ):
    print("One", size, crust, "crust pizza with", sauce, "sauce, topped with", topping + ".")



# (B) To accommodate the customer who wants a bunch of extra toppings, use *args
# write function here
def order_pizza_v2(size, crust, sauce, *topping):
    side_str = ""
    for topping in topping:
        side_str += topping + ", "
    print("One", size, crust, "crust pizza with", sauce, "sauce, topped with", side_str + ".")




# main
# This is the call for the original version
order_pizza_original("large", "cauliflower", "pesto", "sun-dried tomatoes")

# This is the call for Part A
order_pizza("small", "pepperoni")

# This is the call for Part B
order_pizza_v2("medium", "thick", "red", "pepperoni", "spinach", "mushrooms")



