# Mastery Check 2 - Fall 2024
# Taco Truck Ordering System

import random

# SET UP
veggies = [ "spicy tempeh", "refried beans"] #removed tofu
meats = ["ground beef", "pork carnitas", "spicy chicken", "shrimp", "fish", "steak"] #added 3 new meats
toppings = ["Peppers", "Cheese", "Sour Cream", "No toppings"] #changed all of the toppings to new ones and an option for no toppings

items_ordered = []


print("\nWelcome! To I210 Taco Truck! Let's get your order placed.")
name = input("May I have a name for your order: ")


# INPUT / PROCESSING
# choose a tortilla
while True:
    tortilla = input("Would you like a corn or flour tortilla? ")
    items_ordered.append(tortilla + " tortilla")

    # vegetarian?
    is_veg = input("\nAre you vegetarian? (Y / N): ")

    # choose a protein
    if is_veg == "Y":
        proteins = veggies
    else:
        proteins = meats

    num = 1
    for protein in proteins: #made a for loop to go over every protein in meat or veggies regardless of what items there are
        print(f"Choose {num} for {protein}")
        num = num + 1
        

    choice = input("\nWhich protein would you like? ")

    protein = proteins[int(choice) - 1]
    items_ordered.append(protein)

    # choose a topping
    num1 = 1
    for topping in toppings: #made a for loop to over every topping choice no matter what the list has in it
        print(f"Choose {num1} for {topping} ")
        num1 = num1 + 1
    top_choice = input("\nWhich topping would you like? ")

    topping = toppings[int(top_choice) - 1]
    items_ordered.append(topping)

    # salsa?
    salsa_choice = input("\nWould you like spicy salsa on that? (Y / N): ")
    if salsa_choice == "Y":
        salsa = "our spicy salsa"
        items_ordered.append("spicy salsa")
    else:
        salsa = "hold the salsa"

    #guacamole #used the same logic from the salsa choice
    guacamole_choice = input("\nWould you like guacamole on that? (Y / N): ")
    if guacamole_choice == "Y":
        guacamole = "and our guacamole"
        items_ordered.append("guacamole")
    else:
        guacamole = "hold the guacamole"

    # OUTPUT
    # display taco order
    taco_order = "\nOk, that's one {} taco on a {} tortilla with {}, {}, {}."
    print(taco_order.format(protein, tortilla, topping, salsa, guacamole))
    order_again = input("would you like to order another a taco? (Y/N) ")
    if order_again == 'N':
        break


#-------------------------------------------------
print("Thank you for your order.")
print("Help the I210 Taco truck be the best it can be!")
survey_code = random.randint(100000,999999)
print(f"Text survey code {survey_code} to 210-210 to particpate.")
tip = input("would you like to leave a tip? (Y/N): ")
if tip == 'Y':
    tip_amount = input("How much of a tip would you like to leave?: ")
    print(f"Thank you for your generosity and support!")
else:
    print("Thank you and have a great day!")

print(items_ordered)
item_count = {}
for item in items_ordered: #iterates through the items_ordered list and checks if and how much of an item is ordered
    if item not in item_count:  #this checks if the item is not already in item_count
        item_count[item] = 1
    else:
        item_count[item] += 1
print(item_count)