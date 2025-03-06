import random

# functions
def animal_race():
    # initialize values for the remaining distance for each animal
    tortoise_remaining_distance = 20
    hare_remaining_distance = 20
    # Use a loop to run the race until there's a winner
    # Each time the loop runs, each animal moves between 1 and its speed
    # Return the winner and the remaining distance for the loser
    while tortoise_remaining_distance > 0 and hare_remaining_distance > 0:
        tortoise_remaining_distance = tortoise_remaining_distance - random.randint(1,5)
        hare_remaining_distance = hare_remaining_distance - random.randint(1,10)
    if tortoise_remaining_distance > hare_remaining_distance:
        winner = "Hare"
        remaining_distance = "Distance left for opponent", tortoise_remaining_distance
    elif tortoise_remaining_distance < hare_remaining_distance:
        winner = "Tortoise"
        remaining_distance = "Distance left for opponent", hare_remaining_distance
    
    return winner, remaining_distance


# set up - define any global variables here
race_distance = 20
max_tortoise_speed = 5
max_hare_speed = 10


# main

# call the function, receive the return values, and print them here
race = animal_race()
print(race)