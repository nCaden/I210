from random import choice, randint

dance_moves = ["The dougie", "The quan", "The boogie", "The shopping cart", "The two step"]
robot_dance_move = choice(dance_moves)
rating = randint(1, 10)

print(f"{robot_dance_move} has a rating of {rating:.2f}.")