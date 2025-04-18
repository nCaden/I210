# 11.3 counting coins using functions
import random

# (1) write a function "create_cup" 
# that takes an integer for how many coins are in the cup
# and returns a list of coins (listed by name)
# e.g. ['dime', 'quarter', ...]
def create_cup(num_coins):
    types_of_coins = ["penny", "nickel", "dime", "quarter"]
    cup = []
    for i in range(num_coins):
        cup.append(random.choice(types_of_coins))
    return cup
    

# (2) write a function "count_coins" 
# that takes in a list of coins,
# counts the coins and returns a dictionary
# results stored as {type: amount}, e.g. {'dime': 16, ...}
def count_coins(change):
    counted_coins = {}
    for coin in change:
        # if that type of coin isn't in the dictionary, add it
        if coin not in counted_coins:
            counted_coins[coin] = 1
        # if that type of coin is in the dictionary, add to the value
        else:
            counted_coins[coin] += 1
    return counted_coins
  
    

# (3) write a function "print_change" 
# that takes in a dictionary of coins,
# and prints the summary about them.
# There is no need for a return statement!
def print_change(counted_coins):
    quarters = counted_coins["quarter"] * 0.25
    dimes = counted_coins["dime"] * 0.10
    nickels = counted_coins["nickel"] * 0.05
    pennies = counted_coins["penny"] * 0.01
    total = quarters + dimes + nickels + pennies
    print('Quarters: ${:.2f}'.format(quarters))
    print('Dimes: ${:.2f}'.format(dimes))
    print('Nickels: ${:.2f}'.format(nickels))
    print('Pennies: ${:.2f}'.format(pennies))
    print('\nTotal change in cup: ${:.2f}'.format(total))

# SET-UP
types_of_coins = ["penny", "nickel", "dime", "quarter"]

# main

# CREATE A CUP FULL OF CHANGE
change = create_cup(1500)
my_counted_coins = count_coins(change)
my_print_change = print_change(my_counted_coins)
# print(change) 

# COUNT HOW MANY COINS OF EACH TYPE

# print(counted_coins)

# CALCULATE THE MONETARY VALUE
# Question: how many more of these kinds of calculations
# and printing statements would we need before it makes
# sense to also make functions to handle these tasks?
