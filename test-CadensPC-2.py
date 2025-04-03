user_values = [1, 6, 8, 3]

max_value = user_values[0]
for n in range(len(user_values)):
  if user_values[n] >= max_value:
    max_value = user_values[n]
    print(max_value)