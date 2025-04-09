my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number * 3 for number in my_list if (number <= 2) and (number % 2 == 0) ]
print(new_list)