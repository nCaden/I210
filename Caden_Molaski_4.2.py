# 4.2 Animal facts
# compares facts about three animals

# SET UP
# STEP 1 - choose two animals to compare to the cardinal
# STEP 2 - populate the animal2 and animal3 dictinaries with facts about two additional animals. 
#Use animal1 as our guide.

animal1 = {"name": "Cardinal",
            "habitat": "air",
            "diet": "worms",
            "color": "red"}

animal2 = {"name": "Bear",
           "habitat": "forest",
           "diet": "meant and vegetables",
           "color": "brown"}

animal3 = {"name": "Squirrel",
           "habitat": "forest",
           "diet": "nuts",
           "color": "brown"}

# INPUT
# STEP 3 - tell the user the three animals you will be comparing
# STEP 4 - Ask the user for an animal fact to compare (options are habitat, diet or color)
print(f"We will be comparing {animal1['name']}, {animal2['name']}, and {animal3['name']}")
compare = input("Would you like to compare habitat, diet or color?")


# PROCESSING / OUTPUT
# STEP 5 - print out the fact for the cardinal and the other two animals (this is easier with f strings)
print(f"{animal1[compare]}, {animal2[compare]}, and {animal3[compare]}")

#Optional Challenge STEP - answer the question, is that fact the same for all three animals?
print("Is the fact the same for all 3 animals?")
print({animal1[compare]} == {animal2[compare]} == {animal3[compare]})
