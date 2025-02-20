# Codelike 8.3 Bakery order updated


# SET UP
desserts = ["brownies", "pie", "cake"]
gluten_free_desserts = ["brownies", "pie"]
flavors = ["vanilla", "chocolate", "double chocolate"]

print("Place your bakery order:")

# INPUT / PROCESSING
# gluten free?
gluten_free = input("Are you gluten-free? (Y/N): ")

# choose a dessert - ADD FOR LOOP HERE
if gluten_free == "Y":
   gluten_free = gluten_free_desserts
else:
    gluten_free = desserts

#ADD FOR LOOP HERE
for i in range(len(gluten_free)):
    print(f"Choose {i+1} for {gluten_free[i]}")

dessert = int(input("Which dessert would you like? "))

#choose a flavor
print("Now choose a flavor")

#ADD FOR LOOP HERE
for i in range(len(flavors)):
    print(f"Choose {i+1} for {flavors[i]}")

flavor = int(input("Which would you like? "))

#message?
message = ""
is_msg = input("Would you like a message on the dessert? (Y/N):  ")

if is_msg == "Y":
    message = input("Please enter the message: ")


# OUTPUT
# display bakery order

if gluten_free == "Y" and is_msg == "Y":
    print("OK, that's one gluten-free", flavors[flavor-1], gluten_free_desserts[dessert-1], "with the message", message)
elif gluten_free == "N" and is_msg == "Y":
    print("OK, that's one", flavors[flavor-1], desserts[dessert-1], "with the message", message)
elif gluten_free == "Y":
    print("OK, that's one gluten-free", flavors[flavor-1], gluten_free_desserts[dessert-1])
else: 
    print("OK, that's one", flavors[flavor-1], desserts[dessert-1])


