num_list = []

def num_cubed(num_list):
    return [i**3 for i in range(num + 1)]

num = int(input("Choose a number"))
print(num_cubed(5))