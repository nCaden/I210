# paste this test code in one line at a time into the interactive mode
# then answer the questions using complex comparisons

cat1_name = "Simba"
cat1_color = "Orange"
cat1_gender = "Male" 
cat1_age = 4
cat1_breed = "Bengal"
cat1_owner = "Julian"

cat2_name = "Sandy"
cat2_color = "Orange"
cat2_gender = "Female"
cat2_age = 5
cat2_breed = "Persian"
cat2_owner = "Julian"

#1 - Are the cats the same color and breed?
print((cat1_color == cat2_color) and (cat1_breed == cat2_breed))

#2 - Is cat#1 or cat#2 older? 
if cat1_age > cat2_age:
    print(f"{cat1_name} is older.")
elif cat1_age < cat2_age:
    print(f"{cat2_name} is older.")

#3 - Are the cat’s names the same length?
print(len(cat1_name) == len(cat2_name))


#4 - Do the cats have the same owner?
print(cat1_owner == cat2_owner)