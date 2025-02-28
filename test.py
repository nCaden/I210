def print_selected_numbers(count):
   for i in range(count):
      number = int(input())
      if (number % 4) == 0:
         print(number)

num_count = 7
print_selected_numbers(num_count)