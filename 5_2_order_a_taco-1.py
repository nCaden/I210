# 5.2 Order a taco 

# SET UP
veggies = ["chili-fried tofu", "spicy tempeh", "refried beans"]
meats = ["ground beef", "pork carnitas", "spicy chicken"]
toppings = ["radishes", "pickled onion", "cilantro"]

print("Place your taco order:")

# INPUT / PROCESSING
# choose a tortilla
tortilla = input("Would you like a corn or flour tortilla?")

# vegetarian?
vegetarian = input("Are you vegertarian (Y/N):")
if vegetarian == "Y":
   print(f"Choose 1 for {veggies[0]} \nChoose 2 for {veggies[1]} \nChoose 3 for {veggies[2]}")
elif vegetarian == "N":
    print(f"Choose 1 for {meats[0]} \nChoose 2 for {meats[1]} \nChoose 3 for {meats[2]}")


# choose a protein
protein = int(input("Which protein would you like?"))
if vegetarian == 'Y':
    p_choice = veggies[protein-1]
elif vegetarian == 'N':
    p_choice = meats[protein-1]

# choose a topping
print("Now choose a topping:")
print(f"Choose 1 for {toppings[0]} \nChoose 2 for {toppings[1]} \nChoose 3 for {toppings[2]}")
topping = int(input("Which would you like?"))
t_choice = toppings[topping-1]
# salsa?
salsa = input("Would you like spicy salsa on that? (Y/N):")
if salsa == "Y":
    salsa = "our spicy salsa"
else:
    salsa = "no salsa"

# OUTPUT
# display taco order
print(f"Ok, that's one {p_choice} taco on a {tortilla} tortilla with {t_choice} and {salsa}.")




