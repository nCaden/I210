# 4.2 State facts
# compares facts about each state

# SET UP
IN_state = {"name": "Indiana",
            "motto": "Crossroads of America",
            "bird": "cardinal",
            "flower": "peony"}
# 1 - create a dictionary for another state
# 2 - add facts about its name, state motto, bird and flower
MI_state = {"name": "Michigan",
            "motto": "If you seek a pleasant peninsula, look about you",
            "bird": "American Robin",
            "flower": "Apple Blossom"}

# INPUT
# 3 - tell the user what states you will be comparing
# 4 - ask the user for a state fact (assume it is motto, bird or flower)
print("We will be comparing Michigan and Indiana")
compare_fact = input("Which fact would you like to compare?")

# PROCESSING / OUTPUT
# 5 - tell the user what the motto, bird or flower is for each state
#   - (this is easier with f strings)
print(f"The Michigan state fact is {MI_state[compare_fact]}")

# 6 - then compare the facts for both states
# 7 - answer the question, are they the same for both states?
print("Are the facts the same for both?")
print(MI_state[compare_fact] == IN_state[compare_fact])

