# 11.2 gumball machine using functions
import random

# (1) write a function "create_gumball_machine" 
# that takes an integer for how many gumballs are in the machines
# and returns a list of colors (listed by name)
# e.g. ['blue','green' ...]
def create_gumball_machine(num_gumballs):
    types_of_gumballs = ["blue", "green", "yellow", "red"]
    gumball_machine = []
    for i in range(num_gumballs):
        gumball_machine.append(random.choice(types_of_gumballs))
    return gumball_machine
# (2) write a function "count_gumballs" 
# that takes in a list of gumballs,
# counts the gumballs and returns a dictionary
# results stored as {type: amount}, e.g. {'green': 16, ...}
def count_gumballs(gumball_machine):
    counted_gumballs = {}
    for color in gumball_machine:
        # if that type of color isn't in the dictionary, add it
        if color not in counted_gumballs:
            counted_gumballs[color] = 1
        # if that type of color is in the dictionary, add to the value
        else:
            counted_gumballs[color] += 1
    return counted_gumballs
# (3) write a function "print_gumballs" 
# that takes in a dictionary of gumballs,
# and prints the summary about them.
# There is no need for a return statement!
def print_gumballs(counted_gumballs):
    gumball_machine_cost = 50
    blue = counted_gumballs["blue"] * 0.05
    green = counted_gumballs["green"] * 0.06
    red = counted_gumballs["red"] * 0.04
    yellow = counted_gumballs["yellow"] * 0.03

    total = gumball_machine_cost + blue + green + yellow + red

    print('Blue: ${:.2f}'.format(blue))
    print('Green: ${:.2f}'.format(green))
    print('Red: ${:.2f}'.format(red))
    print('Yellow: ${:.2f}'.format(yellow))

    print('\nTotal cost of gumball machine: ${:.2f}'.format(total))



# SET-UP



# main

# CREATE A GUMBALL MACHINE FULL OF GUMBALLS


# print(gumball_machine) 

# COUNT HOW MANY GUMBALLS OF EACH TYPE


# print(gumball_machine)

# CALCULATE THE MONETARY VALUE
# Question: how many more of these kinds of calculations
# and printing statements would we need before it makes
# sense to also make functions to handle these tasks?
machine = create_gumball_machine(200)
counted = count_gumballs(machine)
gumballs = print_gumballs(counted)
