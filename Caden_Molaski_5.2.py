# 5.2 Bakery order 

# SET UP
desserts = ["brownies", "pie", "cake"]
gluten_free_desserts = ["brownies", "pie"]
flavors = ["vanilla", "chocolate", "double chocolate"]

print("Place your bakery order:")

# INPUT / PROCESSING
# gluten free?
gluten_free = input("are you gluten free?: (Y/N)")
if gluten_free == "Y":
    print(f"Choose 1 for {gluten_free_desserts[0]} \nChoose 2 for {gluten_free_desserts[1]}")
    gluten_type = "gluten free"
elif gluten_free == "N":
    print(f"Choose 1 for {desserts[0]} \nChoose 2 for {desserts[1]} \nChoose 3 for {desserts[2]}")
    gluten_type = ""
# choose a dessert
dessert = int(input("Which dessert would you like?"))
if gluten_free == 'Y':
    d_choice = gluten_free_desserts[dessert-1]
elif gluten_free == 'N':
    d_choice = desserts[dessert-1]

# choose a flavor
print("Now choose a flavor:")
print(f"Choose 1 for {flavors[0]} \nChoose 2 for {flavors[1]} \nChoose 3 for {flavors[2]}")
flavor = int(input("Which would you like?"))
f_choice = flavors[flavor-1]
  
# message?
message = input("Would you like a message on the dessert? (Y/N)")
if message == 'Y':
    message = input("Please enter the message:")
        

    # enter message


# OUTPUT
# display bakery order
if message:
    print(f"Ok, that's one {gluten_type} {f_choice} {d_choice} with the message: {message}")
else:
    print(f"Ok, that's one {gluten_type} {f_choice} {d_choice}")




