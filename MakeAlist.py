grocery_list = []

while True:
    add_items = input("Enter in items to your grocery list: ")
    if not add_items:
        break
    grocery_list.append(add_items)


print(grocery_list)
print(f"Your grocery list has {len(grocery_list)} items.")