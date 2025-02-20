## 3.3 Code-like Dinner choices

# Meet the dad. He has several favorite dishes. Some of them he really likes, so he has multiple requests.
dad_choices = ["Curry", "Spaghetti", "Fried Chicken", "Pancakes", "Lasagna", "Stir-Fry", "Curry", "Salad"]

# Meet the kid. He also owns some of his own favorite dishes.
kid_choices = ["Pancakes", "Curry", "Dumplings", "Steak", "Porkchops", "Salmon", "Soup", "Mac and Cheese"]

#1 Make each dinner list only contain one copy of each dinner choice by transforming them into sets
set1 = set(dad_choices)
set2 = set(kid_choices)
#2 What dinner options do the dad and kid have to select from? (List all options found in either list)
print(set1.union(set2))
#3 What dinners are liked by either the dad or the kid, but not both?
print(set1.symmetric_difference(set2))
#4 What dinners does only the dad like?
print(set1.difference(set2))
#5 What dinners do both the dad and the kid like?
print(set1.intersection(set2))
#6 What is your recommendation that they have for dinner?
print("They should have steak and salad!")