
def pizza_party(total_slice, num_friends):
    slices_eaten = 0
    slices_left = total_slice

    #create a loop that loops num of friends times
        #ask friend how many slices they ate
        #subtract friend's slices from slices_left
        #add friend's slices to slices_eaten

    for i in range(1, num_friends + 1):
        friends_slices = int(input(f"Friend {i}, how many slices did you eat? "))
        if friends_slices > total_slice - slices_eaten:
            friends_slices = total_slice - slices_eaten  

        slices_eaten += friends_slices  

    slices_left = total_slice - slices_eaten

    return slices_eaten, slices_left
#ask the user for total cost
total_slice = int(input("How many slices do you have?"))
num_friends = int(input("How many friends will be at your pizza party?"))

my_pizza_party = pizza_party
print(my_pizza_party(total_slice, num_friends))