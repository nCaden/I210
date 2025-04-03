# 12.1 Sandwich order

def sandwich_order(size, bread, protein, veggie, sauce):

    print("One", size, bread, "sandwich with", protein, "and", veggie, "topped with our", sauce, "sauce.")
    
sandwich_order("full", "italian", "tuna", "lettuce", "chipotle")
               

#make a new version with size and bread as default parameters
#make it so users can have as many veggies as they want.


def sandwich_order(protein, sauce, *veggies, size="full", bread = "italian" ):   
    side_str = ""
    for veggie in veggies:
        side_str += veggie + ", "
    print("One", size, bread, "sandwhich with", protein, side_str, "topped with our", sauce, "sauce")    
           
sandwich_order("tuna", "chipotle", "lettuce", "onions", "tomatoes", size = "half", bread = "italian")
