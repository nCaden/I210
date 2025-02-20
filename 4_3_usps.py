# SET UP
mail_dict = {"postcard": 0.35,
            "letter": 0.55,
            "small package": 7.5,
            "medium package": 16.0,
            "large package": 40.23}

distance_dict = {"local": 1, 
                 "in-state": 1.5,
                 "out-of-state": 1.75,
                 "international": 2.25
                }

shipping_dict = {"standard": 1,
                 "priority": 1.75,
                 "first-class": 3
                }

# INPUT
mail_type = input("Welcome to the Post Office! What are you shipping? (postcard, letter, small package, medium package, large package) ")
distance = input("How far will it be shipped? (local, in-state, out-of-state, international) ")
shipping = input("How fast would you like that shipped? (standard, priority, first-class) ")

# PROCESSING / OUTPUT
# 3 - You need to add code to calculate the total cost (use multiplication)
total_cost = mail_dict[mail_type] * distance_dict[distance] * shipping_dict[shipping]
# 4 - You need to add code to output the result to the user.
print(f"Alrighty! To ship a {mail_type} to an address that is in {distance} with {shipping} shipping, the total cost will be ${total_cost:.2f} USD")