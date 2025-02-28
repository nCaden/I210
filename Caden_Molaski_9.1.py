# 9.1 Gumball Machine
import random  # you'll need random for this exercise

# SET-UP
types_of_gumballs = ["blue", "green", "yellow", "red"]
gumball_machine = []
counted_gumballs = {"blue": 0, "green": 0, "yellow": 0, "red": 0}

# Fill the gumball machine with gumballs (create the input)
# randomly create a list of gumball colors to represent your gumball machine
for i in range(500):
    gumball_machine.append(random.choice(types_of_gumballs))

    




print(gumball_machine)

# COUNT HOW MANY COLORS OF EACH TYPE (process the data)
for gumball in gumball_machine:
    if gumball in counted_gumballs:
        counted_gumballs[gumball]+=1
    else:
        counted_gumballs[gumball]=1



# (3) CALCULATE THE MONETARY VALUE OF THE MACHINE

#Machine is $50
#Blue Gumballs are 5 cents
#Red Gumballs are 4 cents
#Yellow Gumballs 3 cents
#Green Gumballs are 6 cents
machine = 50
blue_gumball = counted_gumballs["blue"] * 0.05
red_gumball = counted_gumballs["red"] * 0.04
yellow_gumball = counted_gumballs["yellow"] * 0.03
green_gumball = counted_gumballs["green"] * 0.06

total =  machine + blue_gumball + red_gumball + yellow_gumball + green_gumball
print(f"The total monetary value of the machine is ${total:.2f}")



