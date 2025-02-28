from planet_weight_mod import*
from my_mod_math import*

user_planet = input("which planet would you like to know your weight on?: ")
user_weight = int(input("What is your weight?: "))


if user_planet == "Earth":
    user_weight = (weight_on_earth(user_weight))
elif user_planet == "Moon":
    user_weight = (weight_on_moon(user_weight))
elif user_planet == "Mars":
    user_weight = (weight_on_mars(user_weight))
elif user_planet == "Mercury":
    user_weight = (weight_on_mercury(user_weight))
elif user_planet == "Venus":
    user_weight = (weight_on_venus(user_weight))
elif user_planet == "Jupiter":
    user_weight = (weight_on_jupiter(user_weight))
elif user_planet == "Saturn":
    user_weight = (weight_on_saturn(user_weight))
elif user_planet == "Uranus":
    user_weight = (weight_on_uranus(user_weight))
elif user_planet == "Neptune":
    user_weight = (weight_on_neptune(user_weight))
else:
    print("Invalid planet choice")


print(user_weight)
