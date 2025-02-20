# 4.3 Train travel
# computes the ticket price based on destination, fare type and cabin class

# SET UP
location_dict = {"Baltimore": 93.25,
            "Boston": 135.50,
            "Chicago": 40,
            "Dallas": 67.50,
            "Denver": 57.75,
            "Minneapolis": 55,
            "New Orleans": 78.75,
            "Tampa": 155.25,
            "Toronto": 99.95}

fare_dict = {"adult": 1,
             "child": 0.5,
             "student": 0.8,
             "senior": 0.66,
             "military": 0.25}

cabin_dict = {"standard": 1,
              "buisness": 1.66,
              "sleeper cabin": 4.25}

# INPUT
location = input("Welcome to the Train Depot! Where are you going today? (Baltimore, Boston, Chicago, Dallas, Denver, Minneapolis, New Orleans, Tampa, Toronto) ")
fare_type = input("Which type of fare would you like? (adult, child, student, senior, military)  ")
cabin_type = input("Which cabin class would you prefer? (coach, business, sleeper cabin) ")

# PROCESSING / OUTPUT
# 3 - You need to add code to calculate the total cost (use multiplication)
total_cost = (location_dict[location]*fare_dict[fare_type]*cabin_dict[cabin_type])
# 4 - You need to add code to output the correct result to the user.
print(f"Alrighty! Here is one {fare_type} ticket to {location} in {cabin_type} class, the total cost will be ${total_cost}USD")
