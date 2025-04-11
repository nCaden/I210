file = open('messy_grocery_list.txt', 'r')
lines = file.read()
file.close()
groceries = []
for line in lines.split(","):
    groceries.append((line.strip()))
print(groceries)
