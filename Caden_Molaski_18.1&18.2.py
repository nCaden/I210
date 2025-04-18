with open('codelike_messy_grocery_list.txt', 'r') as file:
    lines = file.readlines()
    grocery_list = [item.strip().capitalize() for line in lines for item in line.split(',')]

grocery_list = list(set(grocery_list))
combinations = []
for i in range(len(grocery_list)):
    for j in range(i + 1, len(grocery_list)):
        combinations.append(f"{grocery_list[i]} {grocery_list[j]}")

with open('grocery_item_combinations.txt', 'w') as output_file:
    for pair in combinations:
        output_file.write(pair + '\n')
