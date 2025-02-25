# Import the random module with an alias
import random as r

# List of possible encounters
encounter_list = ["a wild beast", "a hidden treasure", "an old wizard", "a mysterious stranger"]

# List of possible actions
action_list = ["fight", "flee", "talk", "ignore"]

# Step 1: Random Encounter
# Randomly select an encounter from encounter_list and store it in a variable named encounter
# Your code here
encounter = r.choice(encounter_list)
print(encounter)
# Step 2: Random Action
# Shuffle action_list, then store the action at index 0 in a variable named action
# Your code here
r.shuffle(action_list)
print(action_list[0])
# Step 3: Random Reward
# Randomly choose a number between 1 and 10 and store it in a variable named reward
# Your code here
reward = r.randint(1, 10)
# Step 4: Random Heal
# Use random.uniform to randomly choose a float between 0 and 1, and if it's below 0.2, set a boolean variable named healed to True
# Your code here
healed = r.uniform(0, 1)
if healed< 0.2:
    healed = True
else:
    healed = False
print(healed)

# Print the results
# Print the encounter, the action taken, the reward, and whether the player has been healed
# Your code here
