party_list = []
num_guests = 0
add_guests = input("Add a person to your party list: ")

while len(add_guests) != 0:
    party_list.append(add_guests)
    add_guests = input("Add a person to your party list: ")
    num_guests +=1

print(f"{num_guests} people are coming to your party {party_list}")