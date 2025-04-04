#15.2 recipe ratings

# List of recipe ratings
ratings = [4.5, 3.2, 4.8, 2.1, 3.9, 4.0, 2.8, 4.7, 3.5, 2.9]

# Categorize ratings
categorized_ratings = ["good" if rating >= 4.0 else "bad" for rating in ratings]

# Calculate percentage of good recipes
good_count = categorized_ratings.count("good")
total_count = len(categorized_ratings)
percentage_good = (good_count / total_count) * 100

print(f"Percentage of good recipes: {percentage_good:.1f}%")
