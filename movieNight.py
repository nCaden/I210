dad_movies = ["Die hard", "Jaws", "Alien", "Princess Monoke", "Jurassic World"]
kid_movies = ["Jurassic World", "Princess Monoke", "Dragonball Z", "Kung Fu Panda", "How to Train your Dragon"]

set1 = set(dad_movies)
set2 = set(kid_movies)

print(set1.union(set2))
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
print(set1.intersection(set2))

