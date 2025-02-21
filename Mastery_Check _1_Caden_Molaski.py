# Mastery Check 1 - Fall 2024
# Restaurant Agreement Finder Program

# Data about our friends and the restaurants they like
amir_restaurants = {"Taco Bell", "Wendys", "Avers", "Mother Bears", "Pizza X"}
brett_restaurants = {"Taco Bell", "McDonalds", "KFC", "Noodles", "Avers"}
carmen_restaurants = {"Pizza X", "Wendys", "Qdoba", "Azzip", "Kilroys"}
davon_restaurants = {"Wendys", "Noodles", "Pizza X", "Korea Restaurant", "Little Tibet"}
# Step 1a - Add the restaurants for Eva here
eva_restaurants = {"Texas Roadhouse", "Little Tibet", "Noodles", "Burger King", "Pizza X"}
#added eva's restaurants 
# Step 1b - Print out the restaurants for each friend
print(amir_restaurants)
print(brett_restaurants)
print(carmen_restaurants)
print(davon_restaurants)
print(eva_restaurants)
#out put all of the restaurants
# Data about prices for restaurants
# Step 1c - Add any prices that are missing for Eva's restaurants
prices = {'Avers': "$$", 
          'Azzip': "$",
          'Burger King': "$",
          'KFC': "$", 
          'Kilroys': "$$", 
          'Korea Restaurant': "$$",
          'Little Tibet': "$$",
          'McDonalds': "$", 
          'Mother Bears': "$$", 
          'Noodles': "$", 
          'Pizza X': "$$", 
          'Qdoba': "$$", 
          'Taco Bell': "$",
          'Texas Roadhouse': "$$$", 
          'Wendys': "$"}
#print out the dictionary of prices
print(prices)
# Step 1d - Print the prices out

print("--"*23)
#--------------------------------------
# Part 2 of your code goes below here
which_restaurants = input("Where would you like to eat?: ")

for restaurant in amir_restaurants:
    if which_restaurants in amir_restaurants:
        print(f"Amir also likes {which_restaurants}")
        break
    else:
        break
for restaurant in brett_restaurants:
    if which_restaurants in brett_restaurants:
        print(f"Brett also likes {which_restaurants}")
        break
    else:
        break
for restaurant in carmen_restaurants:
    if which_restaurants in carmen_restaurants:
        print(f"Carmen also likes {which_restaurants}")
        break
    else:
        break
for restaurant in davon_restaurants:
    if which_restaurants in davon_restaurants:
        print(f"Davon also likes {which_restaurants}")
        break
    else:
        break
for restaurant in eva_restaurants:
    if which_restaurants in eva_restaurants:
        print(f"Eva also likes {which_restaurants}")
        break
    else:
        break
for price in prices:
    print(f"It will cost {prices[which_restaurants]} to eat there")
    break

#made a for loop for each person checking to see if that person also likes the restaurants the user inputs

print()
print("--"*23)
#--------------------------------------
#Part 3 of your code goes below here

#Step 3a
#turn Amir into a set
#turn Brett into a set
#find the intersection between those sets
set[amir_restaurants]
set[brett_restaurants]
amir_and_brett = amir_restaurants.intersection(brett_restaurants)
#change to a set and intersected using variable amir_and_brett
#print("The restaurants that Amir and Brett both like are: ")
#print("They should expect to pay:", "or")
print()
print(f"The restaurants that Amir and Brett both like are: {amir_and_brett}")
print(f"They should expect ot pay: {prices['Avers']} or {prices['Taco Bell']}")
#Step 3b
#do the same with Carmen and Eva
set[carmen_restaurants]
set[eva_restaurants]
carmen_and_eva = carmen_restaurants.intersection(eva_restaurants)
#print("There is only one restaurant Carmen and Eva both like. It is: ")
#print("They should expect to pay:")
print()
print(f"There is only one restaurant Carmen and Eva both like. It is: {carmen_and_eva}")
print(f"They should expect to pay: {prices['Pizza X']}")

#Step 3c
#find Carmen and Brett's intersection
carmen_and_brett = carmen_restaurants.intersection(brett_restaurants)
#carmen and brett were already changed to sets so I just needed to setup only the intersection this time
#print("There are no restaurants that Brett and Carmen both like. ")
print(f"There are no restaurants that Brett and Carmen both like. {carmen_and_brett}")
print()
print("--"*23)
#--------------------------------------
#BONUS Section of your code goes below here
set[davon_restaurants]
#davon is the only one not turned into a set yet
all_sets = amir_restaurants.union(brett_restaurants, carmen_restaurants, davon_restaurants, eva_restaurants)
print(f"All of the restaurants: {all_sets}")
