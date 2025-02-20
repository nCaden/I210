# 9.1 Counting coins
import random  # you'll need random for this exercise

# SET-UP
types_of_coins = ["penny", "nickel", "dime", "quarter"]
change = []
counted_coins = {}

# CREATE A CUP FULL OF CHANGE (create the input)
# randomly create a list of coins to represent your PizzaX cup full of change
for i in range(50):
    change.append(random.choice(types_of_coins))
print(change)
    



# COUNT HOW MANY COINS OF EACH TYPE (process the data)
for coin in change:
    if coin in counted_coins:
        counted_coins[coin]+=1
    else:
        counted_coins[coin]=1
print(counted_coins)




# (3) CALCULATE THE MONETARY VALUE (calculate and output)
# use code to answer these questions
# Q: What is the monetary value of each type of coin?
# e.g. if I have 3 dimes, I have $0.30 in dimes
# Q: What is the total amount of money in the change cup?
penny_value = counted_coins["penny"]*0.01
nickel_value = counted_coins["nickel"]*0.05
dime_value = counted_coins["penny"]*0.10
quarter_value = counted_coins["quarter"]*0.25
print(penny_value)
print(nickel_value)
print(dime_value)
print(quarter_value)
   
total = (penny_value + nickel_value + dime_value + quarter_value)
print(total)

